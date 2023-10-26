
"""
Created on Thu Aug 17 14:42:52 2023

@author: AS, strawberry and shortcake.
"""

import os
from statistics import mode

directory = r'C:\sedfit\user data\Life Edit\2023172\25OCT2023\155050'

file_list= os.listdir(directory)

#this lets the user choose how many files they want to include
first_scan_index=int(input("What is the number of the first scan? "))
last_scan_index=int(input("What is the number of the last scan? "))

#this makes a list of channels that can be used as the input for the for loop over channels 
ra_list=input("what are the channels used (please write them as a list of integers separated by commas eg. 1,2,3 )")
channels = [int(channel) for channel in ra_list.split(',')]


#initialize an empty wavelength list
wavelengths = []

#For each filename number, gets the ra1, ra2, ra3 
for channel in channels:
    for scan_index in range(first_scan_index, last_scan_index+1):
               
             # Create the filename based on channel and scan_index
        filename = f"{scan_index:05d}.RA{channel}"
        print(filename)
        full_path = os.path.join(directory, filename)

        if os.path.exists(full_path):
            # Open the file and read the second line
            with open(full_path, "r") as f:
                file_lines = f.readlines()
                second_line = file_lines[1]
                second_line_list = second_line.split()
                second_line_second_last = second_line_list[-2]
                file_number = int(second_line_second_last)
                wavelengths.append(file_number)

setmode = mode(wavelengths)
print(setmode)
