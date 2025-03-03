# ***************************************************************
# Author: Matt Tuohy
# Date: 02/01/2025
# Description: Tests connectivity, focus and position of camera.
# Input: strings, integers
# Output: Photos, video and information about media
# Sources: realpython.com, collaboration on github
# ***************************************************************

# test run

# Welcome to Matt's PiCam test!
# This test is for a single camera on the raspberry pi.

# Ready to start a timelapse? (Y/N): Y

# Enter a whole number for each time increment–days, hours, minutes, seconds.

# Number of days: 7
# Number of hours: 0
# Number of minutes: 0
# Number of seconds: 0

# Take photos for 7 days. Is that right? (Y/N): Y

# Great! How many photos per hour: 5

# Sounds good. I will start at the top of the hour.
# Please don't close this window until process is complete.

# Many hours later ___________________________________________

# Capture complete! Hope everything turns out great!

import time
import valid as v
import os

def main():

    # start
    welcome_mesg()

    if program_start():
        start_mesg()
        total_cap_sec = capture_time_input()
        print(total_cap_sec)
        img_capture_amount(total_cap_sec)
        clear_screen()
        print("Sounds good. I will start at the top of the hour.\n"
              "Please don't close this window until process is complete.")

        capture_timelapse(total_cap_sec)



        print("\nCapture complete! Hope everything turns out great!")
    else:
        print("No worries! Just start the program over when you're ready.")


    # Calculations

    # Functions
def capture_time_input():
    cap_days = v.get_integer("Number of days: ")
    cap_hours = v.get_integer("Number of hours: ")
    cap_min = v.get_integer("Number of minutes: ")
    cap_second = v.get_integer("Number of seconds: ")
    total_seconds = ((cap_days * 86400) + (cap_hours * 3600) + (cap_min * 60)
                     + cap_second)
    return total_seconds

def capture():
    # not in use ...
    """
    Runs the capture photo function
    :return: image, photo of subject
    """
    img_cap = os.system("libcamera-still -o test1.jpg "
                        "--vflip --hflip --shutter 8000")
    return img_cap

def welcome_mesg():
    print("Welcome to Matt's PiCam test!\n"
          "This test is for a single camera on the raspberry pi.")

def program_start():
    start_or_cancel = v.get_yesno_truefalse("Ready to start a timelapse? "
                                            "(Y/N): ")
    return start_or_cancel

def start_mesg():
    print("Enter a whole number for each time increment–days, "
          "hours, minutes, seconds.")

def img_capture_amount(total_cap_seconds):
    photos_per_hour = v.get_integer("Great! How many photos per hour: ")
    total_hours = (total_cap_seconds / 3600)
    total_photos = total_hours * photos_per_hour
    interval = 3600 / photos_per_hour if photos_per_hour > 0 else 0
    print("That's", total_hours, "hours. That's a total of",
          total_photos,".")
    return photos_per_hour, interval

def capture_timelapse(total_cap_seconds):
    total_photos, interval = img_capture_amount(total_cap_seconds)

    for i in range(total_photos):
        # Construct the command to capture an image
        filename = f'timelapse_{i:03d}.jpg'
        command = f'libcamera-still -o {filename} --timeout 1000'

        # Execute the command
        os.system(command)
        print(f'Captured {filename}')

        # Wait for the specified interval before capturing the next photo
        time.sleep(interval)


def clear_screen():
    os.system('clear')


main()