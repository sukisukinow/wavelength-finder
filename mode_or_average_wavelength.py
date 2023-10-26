# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:42:52 2023

@author: SukiHyman
"""

#Save the total
running_total = 0

#Loops over filename numbers from 1 to 20
for i in range(1, 20+1):
               #For each filename number, gets the ra1, ra2, ra3 
               for j in range(1, 3+1):
                              #Turns the filename number into a string
                              filename_string = str(i)
                              #Creates a string of zeros, assuming each filename has 5 total characters
                              filename_chars = 5
                              zero_string = "".join(["0"]*(filename_chars-len(filename_string)))
                              #Gets the extension string
                              extension_string = ".RA" + str(j)

                              #Creates the filename string
                              filename_string = zero_string + filename_string + extension_string

                              #Opens the file
                              f = open(filename_string, "r")
                              file_lines = f.readlines()
                              second_line = file_lines[1]

                              #Gets the line number as a string
                              second_line_list = second_line.split()
                              second_line_second_last = second_line_list[-2]

                              #Converts the line number to a number and adds to the running total
                              file_number = int(second_line_second_last)
                              
                              set=[]
                              set.append(file_number)

                              running_total = running_total+file_number

#20 filenumbers, 3 extensions per file means 60 items should have been gotten
setmode =  mode(set)
print(setmode)
