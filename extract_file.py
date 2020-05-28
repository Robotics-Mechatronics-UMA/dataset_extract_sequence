from os import listdir, getcwd
from os.path import isfile, isdir, join

#from single_extract_options import SingleExtractOptions
from extract_file_options import FileExtractOptions
from extract_sequence import SingleSequence

# Global variables for arguments and path
options = FileExtractOptions()
opts = options.parse()
cwd = getcwd()


def file_parser(filename):

    sequences = []

    with open(filename, 'r') as f:

        for line in f:

            output, folder, devices, data_formats, intervals = line.split('/')

            for interval in intervals.strip().split():
                start = float(interval.split(':')[0])
                end = float(interval.split(':')[1])
                if end == -1 :
                    #print("End set to: " + str(float("inf")))
                    end = float("inf")
                sequence = SingleSequence(join(cwd, output.strip()), join(
                    cwd, folder.strip()), devices.strip().split(), data_formats.strip().split(), start, end)
                #print("Added sequence with: " + str(sequence.start) + " and " + str(sequence.end))
                sequences.append(sequence)

    return sequences


if __name__ == "__main__":

    sequences = file_parser(opts.filename)

    for sequence in sequences:
        sequence.extract()
