from os import listdir, getcwd, mkdir, makedirs
from os.path import isfile, isdir, join, splitext
from shutil import copyfile
import io


class SingleSequence:
    """
        Class to extract a single sequence.
    """

    def __init__(self, output, folder, devices, datatypes, start, end, verbose_print=lambda *a: None, sequencing=False):
        self.output = output
        self.folder = folder
        self.devices = devices
        self.datatypes = datatypes
        self.start = start
        self.end = end
        self.verbose_print = verbose_print
        self.sequencing = sequencing

        if self.sequencing : self.seq_numbers = {}

        self.list_directories()
        self.create_output_directories()

    def list_directories(self):
        """
            Method to list all the directories to extract data from.
        """
        if(len(self.devices) != len(self.datatypes)):
            self.verbose_print("ERROR: DEVICES AND DATATYPES MISMATCH!!")

        self.directories = []

        for idx, device in enumerate(self.devices):
            self.verbose_print("Device added: " + device)
            self.directories.append(DataDirectory(device, self.datatypes[idx]))

    def create_output_directories(self):
        """
            Method to create the directories to extract the data.
        """
        
        if not isdir(self.output):
            makedirs(self.output)

            for directory in self.directories:
                mkdir(join(self.output, directory.device))
                self.verbose_print("Created directory: " +
                                   join(self.output, directory.device))

    def get_timestamp_txt(self, line):
        """
            Method to get the timestamp from data.txt
        """
        timestamp = float(line.split()[0])

        return timestamp

    def get_timestamp_filename(self, filename):
        """
            Method to get the timestamp from a filename
        """
        name, _ = splitext(filename)
        print("Extracting:" + filename)
        timestamp = float(name.split('-')[1])

        return timestamp

    def extract_data(self, directory):
        """
            Method to chose the extraction method.
        """
        if directory.datatype == 'single_file':
            self.extract_data_single(directory)

        elif directory.datatype == 'multiple_files':
            self.extract_data_multi(directory)

        else:
            self.verbose_print("ERROR DATATYPE NOT RECOGNISED!!")

    def extract_data_single(self, directory):
        """
            Method to extract part of a input data.txt file and copy it to the output data.txt.
        """
        # Get the name for the input file: /folder/device/data.txt
        input_file_name = join(self.folder, directory.device, 'data.txt')

        # Get the name for the output file: /output/device/data.txt
        output_file_name = join(self.output, directory.device, 'data.txt')

        # Open both files
        with open(input_file_name, 'r') as input_file, open(output_file_name, 'a+') as output_file:
            for line in input_file:
                timestamp = self.get_timestamp_txt(line)
                if(timestamp >= self.start and timestamp <= self.end):
                    # self.verbose_print("As: " + str(timestamp) + " is in between: " + str(self.start) + " and " + str(self.end))
                    self.verbose_print("Written: " + line)
                    output_file.write(line)

                    if self.sequencing: self.register_sequence(directory, timestamp)
                        

    def extract_data_multi(self, directory):

        files = sorted(listdir(join(self.folder, directory.device)))
        # List the directory files.
        for filename in files:

            # Separate sequence, timestamps and extension.
            timestamp = self.get_timestamp_filename(filename)

            if(timestamp >= self.start and timestamp <= self.end):
                # self.verbose_print("As: " + str(timestamp) + " is in between: " + str(self.start) + " and " + str(self.end))
                self.verbose_print("Copied: " + filename)
                copyfile(join(self.folder, directory.device, filename),
                         join(self.output, directory.device, filename))

                if self.sequencing: self.register_sequence(directory, timestamp)

    def extract(self, seq_numbers):
        """
            Method to extract all data from a single folder.
        """
        if self.sequencing:
            self.seq_numbers = seq_numbers
            for directory in self.directories:
                if not (directory.device in seq_numbers) : seq_numbers[directory.device] = 0

        for directory in self.directories:
            self.extract_data(directory)
            self.verbose_print('Extracted: ' + directory.device)

    def register_sequence(self, directory, timestamp):
        with open(join(self.output, '..', 'translation_file_{}.txt'.format(directory.device)), 'a+') as translation_file:
            self.seq_numbers[directory.device] += 1
            translation_file.write("{:010} {:.6f}\n".format(self.seq_numbers[directory.device],timestamp))

class DataDirectory:
    """
        Structure to store directory related data for each device.
    """

    def __init__(self, device, datatype):
        self.device = device
        self.datatype = datatype
