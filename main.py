# ***************************************************************
# Author: Matt Tuohy
# Date: 8/6/2024
# Description: Pi-camera code used to make time-lapse videos over
# long periods of time.
# Input: duration in days, hours and minutes, file names
# Output: Photos, video and information about media
# Sources: realpython.com, collaboration on github
# ***************************************************************

# Test run

# Good morning! Ready to start a new timelapse? Good.
# Resuming previous project? (Y/N): N
# Enter the name of the new project: sprouting_seed
# Would you like 30, 60 0r 120 frames per second: 30

# Let's make sure everything is in focus for each camera (use
# arrow keys to adjust focus on next preview screens)

# 'Would you like a rendered timelapse video at the end of each day? (Y/N): Y'
# When should the camera stop capturing in days?: 5
# When should the camera stop capturing in hours?: 5
# When should the camera stop capturing in minutes?: 5

# Ready to start? (Y/N): yes

# starting timelapse

# end of day 1, 1000 images captured, 1 video made
# end of day 2, 1000 images captured, 1 video made
# end of day 3, 1000 images captured, 1 video made
# end of day 4, 1000 images captured, 1 video made
# end of day 5, 1000 images captured, 1 video made

# Timelapse complete!

import time
import valid as v
import cv2


def main():
    # Camera test
    camera_index = 0


    # List available cameras
    cameras = list_cameras()
    print("Available cameras: ", cameras)

    # calculations

    # output

    # functions


def list_cameras(max_cameras=4):
    available_cameras = []
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()  # Release the camera
    return available_cameras


def capture_time():
    print("Let's figure out how long this timelapse should take.")
    capture_days = v.get_integer(
        'When should the camera stop capturing in number of days?: ')
    capture_hours = v.get_integer(
        'When should the camera stop capturing in hours?: ')
    capture_min = v.get_integer('When should the camera stop capturing in '
                                'minutes?: ')

    return [capture_days, capture_hours, capture_min]


def project_name():
    get_project_name = v.get_string('Please name the project: ')
    return get_project_name


def focus_check():
    in_frame = v.get_y_or_n('Is everything in focus and in frame? (Y/N): ')
    return in_frame


def start_capture():
    start_cap = v.get_y_or_n('Ready to start? (Y/N): ')
    return start_cap


main()
