# Extract sequence

## Overview
Script to extract a sub-sequence from a dataset composed of folder for each device and data in one data.txt file or multiple files.

## Installation

Just clone the repository and check the dependencies.

### Dependencies

* Python 3.5
* Python packages:
    * os
    * argparse
    * shutil

## Contents

* `*_options:` the scripts to store the options for 'argparse'.
* `extract_sequence:` class to extract data from a single sequence (e.g. folder).
* `extract_single:` script to extract data from a single sequence. It recieves several options (see [Single extraction options](https://github.com/davdmc/extract_sequence#single-extraction-options) or [extract_single_options.py](https://github.com/davdmc/extract_sequence/blob/master/extract_single_options.py)).
* `extract_file:` script to automate the process of extracting data from multiple sequences. It uses a .txt file as a single parameter with a specific format to describe the different sequences that can be shared and edited (see [Extraction format](https://github.com/davdmc/extract_sequence#extraction-format) or [extraction_format.txt](https://github.com/davdmc/extract_sequence/blob/master/extraction_format.txt)).

## Usage

In the case of `extract_single`, you have to specify all the needed arguments. There are different examples in `tests_single.txt`:

    python extract_from_file.py -o output/ -f input/ -d imu -t single_file --start 1559735717.606276 --end 1559735717.720282

In the case of `extract_file`, you have to create a .txt file to store the information about the extraction in the right format (see [Extraction format](https://github.com/davdmc/extract_sequence#extraction-format) or [extraction_format.txt](https://github.com/davdmc/extract_sequence/blob/master/extraction_format.txt)). There is an example in the file `test_sequence.txt`:

    python extract_file.py -f test_file.txt

## Single extraction options

- `-o/--output:` Output sequence name (i.e. relative path).

- `-f/--folder:` Objective folder to extract from.

- `-d/--device_list:` Spaced separated list with the aimed devices.

- `-t/--data_formats:` Format to extract files from {single_file / multiple_files}.

- `--start:` Start time for the sequence.

- `--end:` End time for the sequence.

- `-v/--verbose:` Optional parameter to print additional info for debug purposes.

## Extraction format

In order to ease the extraction of multiple sequences in a shareable format, a file based method is implemented. Each line corresponds to a sequence that can have the same name. The format uses `|` , ` ` or `:` separators and there must be no blank lines. 

Each line is:

```
output | folder | device1,device2 ... | format1, format2 ... | interaval 1, interval 2 ...
```

### Output

The relative path and name (to the script execution directory) for the output sequence (e.g. folder). If it already exists, it will add the data appending to the existent data.txt and merging (with override if it exists) of the files for the already existent devices.

### Folder

The relative path and name (to the script execution directory) for the input sequence to be splitted. It is assumed to have the following format:

    sequence/
        device1/
            data.txt                (if single file)
        device2/
            device-tmstmp1.ext     (if multiple files)
            device-tmstmp1.ext
            .
            .
            .
        device3/
        .
        .
        .

### Devices

It corresponds to directories under the folder parameter and is understood as different data sources.

The number of devices and formats must be the same.

### Formats

The format can be:

* single_file: in case that the data is stored in a data.txt file. The structure of the data inside the file is expected to be:

        timestamp data1 data2 data3 ...

* multiple_files: in case that the data is stored in multiple files. The filename of the data is expected to be:

        device-timestamp.extension

### Interval

Each interval is of type:

    start:end

The units must be the same as in the data as they are compared.

Using -1 as start or end means that there is no low or up bound.