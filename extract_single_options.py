from os import listdir, getcwd
import argparse


class SingleExtractOptions():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Arguments for the sequence generation')

        self.parser.add_argument('-o', '--output', type=str,
                                 help='Output sequence name', required=True)
        self.parser.add_argument('-f', '--folder', type=str,
                                 help='Objective folder', required=True)
        self.parser.add_argument('-d', '--device_list', type=str, nargs='+',
                                 help='Delimited list with the aimed devices', required=True)
        self.parser.add_argument('-t', '--data_formats', type=str, nargs='+',
                                 help='Format to extract files from', required=True)
        self.parser.add_argument('--start', type=float,
                                 help='Start time for the sequence', required=True)
        self.parser.add_argument('--end', type=float,
                                 help='End time for the sequence', required=True)
        self.parser.add_argument('-v', '--verbose', type=bool,
                                 help='Optional parameter to print additional info for debug purposes.', default=False)

    def parse(self):
        self.options = self.parser.parse_args()
        return self.options