from os import listdir, getcwd
from os.path import isfile, isdir, join, splitext
from shutil import copyfile
import io


class SingleSequence:
    """
        Class to extract a single sequence.
    """

    def __init__(self, output, folder, devices, datatypes, start, end, exclude="", pop_limits=False):
        self.output = output
        self.folder = folder
        self.devices = devices
        self.datatypes = datatypes
        self.start = start
        self.end = end
        self.exclude = exclude
        self.pop_limits = pop_limits

        self.list_directories()

    def list_directories(self):
        """
            Method to list all the directories to extract data from.
        """
        if(len(self.devices) != len(self.datatypes)):
            print("ERROR: DEVICES AND DATATYPES MISMATCH!!")

        self.directories = []

        for idx, device in enumerate(self.devices):
            self.directories.append(DataDirectory(device, self.datatypes[idx]))

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
        timestamp = float(name.split('_')[1])

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
            print("ERROR DATATYPE NOT RECOGNISED!!")

    def extract_data_single(self, directory):
        """
            Method to extract part of a input data.txt file and copy it to the output data.txt.
        """
        # Get the name for the input file: /folder/device/data.txt
        input_file_name = self.folder + directory.device + '/data.txt'

        # Get the name for the output file: /output/device/data.txt
        output_file_name = self.output + directory.device + '/data.txt'

        # Open both files
        with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
            for line in input_file:
                timestamp = self.get_timestamp_txt(line)
                if(timestamp >= self.start and timestamp <= self.end):
                    print("Written: " + line)
                    output_file.write(line)

    def extract_data_multi(self, directory):

        # List the directory files.
        for filename in listdir(self.folder + directory.device + '/'):

            # Separate sequence, timestamps and extension.
            timestamp = self.get_timestamp_filename(filename)

            if(timestamp >= self.start and timestamp <= self.end):
                print("Copied: " + filename)
                copyfile(join(self.folder, directory.device, filename),
                         join(self.output, directory.device, filename))

    def extract(self):
        """
            Method to extract all data from a single folder.
        """
        for directory in self.directories:
            self.extract_data(directory)
            print('Extracted: ' + directory.device)


class DataDirectory:
    """
        Structure to store directory related data for each device.
    """

    def __init__(self, device, datatype):
        self.device = device
        self.datatype = datatype


if __name__ == "__main__":

    print("HEllo")
