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

import valid as v

def main():

    # start

    welcome_mesg()

    while program_start():
        start_mesg()
        cap_d()
        cap_h()
        cap_m()
        cap_s()
        img_capture_amount()

        print("Sounds good. I will start at the top of the hour.\n"
              "Please don't close this window until process is complete.")

        # _______START_HERE________
        # Run camera capture program here

        print("Capture complete! Hope everything turns out great!")
    else:
        print("No worries! Just start the program over when you're ready.")


    # Calculations

    # Functions
def welcome_mesg():
    print("Welcome to Matt's PiCam test!\n"
          "This test is for a single camera on the raspberry pi.")

def program_start():
    start_or_cancel = v.get_yesno_truefalse("Ready to start a timelapse? (Y/N): ")
    return start_or_cancel

def start_mesg():
    print("Enter a whole number for each time increment–days, hours, minutes, seconds.")

def cap_d():
    cap_days = v.get_integer("Number of days: ")
    return cap_days

def cap_h():
    cap_hours = v.get_integer("Number of hours: ")
    return cap_hours

def cap_m():
    cap_min = v.get_integer("Number of minutes: ")
    return cap_min

def cap_s():
    cap_second = v.get_integer("Number of seconds: ")
    return cap_second

def img_capture_amount():
    photos_per_hour = v.get_integer("Great! How many photos per hour: ")
    return photos_per_hour


main()