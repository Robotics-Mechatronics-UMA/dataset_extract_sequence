from os import listdir, getcwd
from os.path import isfile, isdir, join

from extract_single_options import SingleExtractOptions
from extract_sequence import SingleSequence

# Global variables for arguments and path
options = SingleExtractOptions()
opts = options.parse()
cwd = getcwd()

if __name__ == "__main__":

    sequence = SingleSequence(join(cwd, opts.output), join(cwd, opts.folder), opts.device_list,
                              opts.data_types, opts.start, opts.end, opts.verbose)

    sequence.extract()