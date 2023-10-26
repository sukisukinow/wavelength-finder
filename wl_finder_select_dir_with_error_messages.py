import os
from statistics import mode, mean
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Use a file dialog to select the directory
directory = filedialog.askdirectory()
if not directory:
    print("No directory selected. Exiting.")
else:
    file_list = os.listdir(directory)

    # This lets the user choose how many files they want to include
    first_scan_index = int(input("What is the number of the first scan? "))
    last_scan_index = int(input("What is the number of the last scan? "))

    # This makes a list of channels that can be used as the input for the for loop over channels
    ra_list = input("What are the channels used (please write them as a list of integers separated by commas eg. 1,2,3 )")
    channels = [int(channel) for channel in ra_list.split(",")]

    # Initialize an empty dictionary to store the wavelengths, modes, and averages for each channel
    channel_stats = {}

    # For each filename number, get the ra1, ra2, ra3
    for channel in channels:
        # Initialize empty lists for the current channel
        wavelengths = []

        for scan_index in range(first_scan_index, last_scan_index + 1):
            # Create the filename based on channel and scan_index
            filename = f"{scan_index:05d}.RA{channel}"
            full_path = os.path.join(directory, filename)

            if not os.path.exists(full_path):
                print(f"Warning: File {filename} not found in channel {channel}. Skipping.")
                continue  # Skip processing this channel

            # Open the file and read the second line
            with open(full_path, "r") as f:
                file_lines = f.readlines()
                second_line = file_lines[1]
                second_line_list = second_line.split()
                second_line_second_last = second_line_list[-2]
                file_number = int(second_line_second_last)
                wavelengths.append(file_number)

        # Check if the number of files in the selected channel exceeds available files with the matching extension
        if len(file_list) < last_scan_index - first_scan_index + 1:
            print(f"Warning: Data is out of range for channel {channel}. Skipping.")
            continue

        # Calculate the mode for the current channel's wavelength list
        if wavelengths:
            channel_modes = {
                'mode': int(mode(wavelengths)),
                'average': int(mean(wavelengths))
            }
            # Store the modes and averages in the dictionary with keys like "channel_1_mode" and "channel_1_average"
            channel_stats[f'channel_{channel}'] = channel_modes

    # Print the modes and averages for each channel
    for channel, stats in channel_stats.items():
        print(f'{channel} - Mode: {stats["mode"]}, Average: {stats["average"]}')
