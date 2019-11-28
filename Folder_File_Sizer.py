# Script Name   : file_sizer.py
# Author        : Serdar Ilarslan
# Created       : 28th November 2019
# Last Modified	: 28th November 2019
# Version       : 1.0.0

# Modifications : None

# Description   : This will scan the current directory and all subdirectories and display the size.

import os
import sys

try:
    directory = sys.argv[1] # Set the variable as path of the directory user had provided
    if os.path.isdir(str(directory)):
        pass
    else:
        print("Directory entered doesn't exist!")
except IndexError:
    print("Must provide an argument!")

directory_size = 0 # Initialize the directory total size to int(0)
megabites_unit = float(1) / (1024 * 1024)
files_size = {}

for path, dirs, files in os.walk(directory):
    for file in files:
        file_name = os.path.join(path,file)
        file_size = os.path.getsize(file_name)
        files_size[file_name] = file_size
        directory_size += file_size

print("--------------------------------------\n\n")
print("Total size of the directory: " + str(round((directory_size * megabites_unit),4)) + "MB")
print("\n--------------------------------------\n")
for key in files_size:
    print(str(key) + ": " + str(round((files_size[key] * megabites_unit), 4)) + "MB")
print("--------------------------------------")
