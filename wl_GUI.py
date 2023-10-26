import os
from statistics import mode, mean
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Entry, Button, Text

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Create a Tkinter window for entering scan indices and displaying results
input_window = tk.Toplevel(root)
input_window.title("Scan Indices and Results")

def on_closing():
    root.quit()


# Bind the closing event of the input window
input_window.protocol("WM_DELETE_WINDOW", on_closing)

first_scan_index_label = Label(input_window, text="First Scan Index:")
first_scan_index_label.pack()

first_scan_index_entry = Entry(input_window)
first_scan_index_entry.pack()

last_scan_index_label = Label(input_window, text="Last Scan Index:")
last_scan_index_label.pack()

last_scan_index_entry = Entry(input_window)
last_scan_index_entry.pack()

channels_label = Label(input_window, text="Channels (comma-separated):")
channels_label.pack()

channels_entry = Entry(input_window)
channels_entry.pack()

results_text = Text(input_window, height=10, width=50)
results_text.pack()

def calculate_modes_and_averages():
    first_scan_index = int(first_scan_index_entry.get())
    last_scan_index = int(last_scan_index_entry.get())
    
    channels = [int(channel) for channel in channels_entry.get().split(",")]
    
    if not channels:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "No channels provided. Please enter at least one channel.")
        return

    directory = filedialog.askdirectory()
    if not directory:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "No directory selected. Exiting.")
        return

    file_list = os.listdir(directory)
    
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

            if os.path.exists(full_path):
                # Open the file and read the second line
                with open(full_path, "r") as f:
                    file_lines = f.readlines()
                    second_line = file_lines[1]
                    second_line_list = second_line.split()
                    second_line_second_last = second_line_list[-2]
                    file_number = int(second_line_second_last)
                    wavelengths.append(file_number)

        # Calculate the mode and average for the current channel's wavelength list
        if wavelengths:
            channel_modes = {
                'mode': int(mode(wavelengths)),
                'average': int(mean(wavelengths))
            }
            # Store the modes and averages in the dictionary with keys like "channel_1" and "channel_2"
            channel_stats[f'channel_{channel}'] = channel_modes

    # Print the modes and averages for each channel in the results_text
    results_text.delete(1.0, tk.END)
    for channel, stats in channel_stats.items():
        results_text.insert(tk.END, f'{channel} - Mode: {stats["mode"]}, Average: {stats["average"]}\n')

# Create a button to calculate modes and averages
calculate_button = Button(input_window, text="Calculate Modes and Averages", command=calculate_modes_and_averages)
calculate_button.pack()

# Start the Tkinter main loop
root.mainloop()
