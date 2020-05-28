from os import listdir, getcwd
import argparse


class FileExtractOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Arguments for the sequence generation')

        self.parser.add_argument('-f', '--filename', type=str,
                                 help='Extraction file name', required=True)

    def parse(self):
        self.options = self.parser.parse_args()
        return self.options