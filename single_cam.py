# ***************************************************************
# Author: Matt Tuohy
# Date: 02/01/2025
# Description: Tests connectivity, focus and position of camera.
# Input: strings, integers
# Output: Photos, video and information about media
# Sources: w3schools.org, collaboration on github
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

# ___what the code is doing___:
# capture photo
# determine if photo is bright enough to use
# Discard or use photo
# Add photo to folder for the day
# at end of the day, create timelapse video of the captures
# add video to video folder

# Please don't close this window until process is complete.

# Many hours later ___________________________________________

# Capture complete! Hope everything turns out great!


import time
import valid as v
import os
from datetime import datetime, timedelta
from astral import LocationInfo
from astral.sun import sun


def main():
    # constants

    # Set location
    city = LocationInfo("Portland" , "USA")
    s = sun(city.observer, date=datetime.now())

    # sunrise and sunset times
    sunrise = s["sunrise"]
    sunset = s["sunset"]

    start_time = sunrise + timedelta(hours=1)
    stop_time = sunset - timedelta(hours=1)

    # start
    welcome_mesg()

    # menu
    if program_start():
        start_mesg()

        #___USE FOR GETTING PHOTO CAPTURE LENGTH___
        # total_cap_sec = capture_time_input()
        # photos_ph = photos_per_hour()
        # total_photos(total_cap_sec, photos_ph)

        while True:
            now = datetime.now()

            if start_time <= now <= stop_time:
                capture()
            else:
                print("Something went wrong. Try again.")

            time.sleep(60)

    else:
        print("No worries! Just start the program over when you're ready.")


    # Functions
def capture_time_input():
    """
    Get the amount of time in various increments
    :return: int, total amount of seconds the program will run.
    """
    cap_days = v.get_integer("Number of days: ")
    cap_hours = v.get_integer("Number of hours: ")
    cap_min = v.get_integer("Number of minutes: ")
    cap_second = v.get_integer("Number of seconds: ")
    total_seconds = ((cap_days * 86400) + (cap_hours * 3600) + (cap_min * 60)
                     + cap_second)
    return total_seconds

def capture():
    # using for testing
    """
    Runs the capture photo function
    :return: image, photo of subject
    """
    img_cap = os.system("libcamera-still -o test1.jpg "
                        "--vflip --hflip --shutter 8000")
    return img_cap

def welcome_mesg():
    """
    Message that shows the program is on and running
    :return: none
    """
    print("Welcome to Matt's PiCam test!\n"
          "This test is for a single camera on the raspberry pi.")

def program_start():
    """
    Confirms that the user would like to start the program, allows to start
    over if not.
    :return: true/false
    """
    start_or_cancel = v.get_yesno_truefalse("Ready to start a timelapse? "
                                            "(Y/N): ")
    return start_or_cancel

def start_mesg():
    """
    Instructions on how to proceed with giving capture times.
    :return: none
    """
    print("Enter a whole number for each time increment: days, "
          "hours, minutes, seconds.")

def photos_per_hour():
    photos_ph = v.get_integer("Great! How many photos per hour: ")
    return photos_ph

def total_photos(total_cap_seconds, photos_ph):
    total_hours = (total_cap_seconds / 3600)
    total_photo_number = total_hours * photos_ph
    return total_photo_number

def img_capture_amount(total_cap_seconds, photos_ph):
    """
    START HERE calculate how often a photo needs to be captured
    :param total_cap_seconds:
    :param photos_ph:
    :return:
    """
    total_hours = (total_cap_seconds / 3600)
    interval = total_hours / photos_ph if photos_ph > 0 else 0
    print(f"That's {interval} per hour.")
    return interval

def capture_timelapse(total_ph, interval):
    for i in range(total_ph):
        # Construct the command to capture an image
        filename = f'timelapse_{i:03d}.jpg'
        command = f'libcamera-still -o {filename} --timeout 1000'

        # Execute the command
        os.system(command)
        print(f'Captured {filename}')

        # Wait for the specified interval before capturing the next photo
        time.sleep(interval)


def clear_screen():
    """
    clears the terminal screen to keep things up to date and clutter-free
    :return: none
    """
    os.system('clear')


main()