from os import listdir, getcwd
from os.path import isfile, isdir, join

from extract_single_options import SingleExtractOptions
from extract_sequence import SingleSequence

# Global variables for arguments and path
options = SingleExtractOptions()
opts = options.parse()
cwd = getcwd()

# Add a print option
if opts.verbose:
    def verbose_print(*args):
        for arg in args:
            print(arg)
else:
    verbose_print = lambda *a: None

if __name__ == "__main__":

    seq_numbers = {}

    sequence = SingleSequence(join(cwd, opts.output), join(cwd, opts.folder), opts.device_list,
                              opts.data_types, opts.start, opts.end, verbose_print, opts.sequencing)

    sequence.extract(seq_numbers)