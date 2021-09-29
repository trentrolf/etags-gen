#!/usr/bin/python3

import subprocess
import configparser
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest="filename", help="Input file INI format.", metavar="FILE", required=True)
parser.add_argument('-o', dest="outfilename", help="Output TAGS file.", metavar="FILE")
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.filename)

include_paths = config['etags-gen-config']['include-paths'].split()
include_extensions = config['etags-gen-config']['include-extensions'].split()
exclude_paths = config['etags-gen-config']['exclude-paths'].split()

etags_cmd = ['etags']

if args.outfilename is not None:
    etags_cmd.append('-o')
    etags_cmd.append(args.outfilename)

for include_path in include_paths:
    for root, subdirs, files in os.walk(include_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.splitext(filename)[1] in include_extensions:
                excluded_file = False
                # File is in include list and has an include extension
                # Now check for exclusions
                for exclude_path in exclude_paths:
                    if exclude_path in file_path:
                        exlcuded_file = True

                if not excluded_file:
                    etags_cmd.append(file_path)

# print(*etags_list, sep = "\n")

subprocess.run(etags_cmd)
