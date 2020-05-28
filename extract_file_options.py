from os import listdir, getcwd
import argparse


class FileExtractOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Arguments for the sequence generation')

        self.parser.add_argument('-f', '--filename', type=str,
                                 help='Extraction file name', required=True)
        self.parser.add_argument('-v', '--verbose', type=bool,
                                 help='Optional parameter to print additional info for debug purposes.', default=False)
    def parse(self):
        self.options = self.parser.parse_args()
        return self.options