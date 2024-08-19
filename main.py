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
from picamera import PiCamera


def main():
    # Naming cameras
    num_cameras = []
    num_cameras = 4

    # input

    capture_days = v.get_integer(
        'When should the camera stop capturing in days?: ')

    capture_hours = v.get_integer('# When should the camera stop capturing '
                                  'in hours?: ')

    capture_min = v.get_integer('# When should the camera stop capturing '
                                'in days?: ')

    project_name = v.get_string('Please name the project: ')

    rendering = v.get_y_or_n('Would you like a rendered timelapse video at '
                             'the end of each day? (Y/N): ')

    in_frame = v.get_y_or_n('Is everything in focus and in frame? (Y/N): ')

    start = v.get_y_or_n('Ready to start? (Y/N): ')

    # calculations

    # output


main()
