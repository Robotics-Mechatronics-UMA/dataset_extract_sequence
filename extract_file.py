from os import listdir, getcwd
from os.path import isfile, isdir, join

#from single_extract_options import FileExtractOptions
from extract_file_options import FileExtractOptions
from extract_sequence import SingleSequence

# Global variables for arguments and path
options = FileExtractOptions()
opts = options.parse()
cwd = getcwd()

# Add a print option
if opts.verbose:
    def verbose_print(*args):
        for arg in args:
            print(arg)
else:
    verbose_print = lambda *a: None

def file_parser(filename, verbose=False):
    '''
        Extract the data from the extraction file and returns a sequence list.
    '''
    sequences = []

    with open(filename, 'r') as f:

        for line in f:

            output, folder, devices, data_formats, intervals = line.split('|')

            for interval in intervals.strip().split():
                start = float(interval.split(':')[0])
                end = float(interval.split(':')[1])

                # Use the maximum time.
                if end == -1 :
                    end = float("inf")

                # Create a single sequence object from the data.
                sequence = SingleSequence(join(cwd, output.strip()), join(
                    cwd, folder.strip()), devices.strip().split(), data_formats.strip().split(), start, end, verbose, opts.sequencing)
                verbose_print("Added sequence with: " + str(sequence.start) + " and " + str(sequence.end))
                sequences.append(sequence)

    return sequences


if __name__ == "__main__":
    
    # Create a persistent sequence number list across all the sequences.
    seq_numbers = {}

    # Create the sequence list.
    sequences = file_parser(opts.filename, verbose_print)

    # Extract each sequence separatedly.
    for sequence in sequences:
        sequence.extract(seq_numbers)
