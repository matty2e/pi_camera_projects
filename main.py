# ***************************************************************
# Author: Matt Tuohy
# Date: 8/6/2024
# Description: Pi-camera code used to make time-lapse videos over
# long periods of time.
# Input: duration in days, hours and minutes, file names
# Output: Photos, video and information about media
# Sources: realpython.com, collaboration on github
# ***************************************************************
import os
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
import os


def main():
    # Camera test
    camera_index = 0

    # List available cameras
    cameras = list_cameras()

    print("Available cameras: ", cameras)

    # Set up project

    project_name = get_project_name()
    in_focus = focus_check()
    start_project = start_capture()
    create_folders = project_folders(project_name)

    # Capture Photos:

    # Each camera is going to need its own name and file name. They are
    # listed as a,b,c and d on the physical board. Because photos are not
    # taken at the same time, it may be best to have the cameras perform
    # their capture before processing them-cannot take pictures
    # simultaneously due to hardware limitations-which means that there will
    # be a delay between pictures.

    # Processing Photos:
        # Time offset for each camera
        # Store files
        # Name files
        # Store files

    # Output:

    # generate timelapse from stills at the end of each day

    # functions


def list_cameras(max_cameras=4):
    """
    Define cameras and give them names.
    :param max_cameras: The amount of cameras that I have set up.
    :return: camera names that align with the hardware labels.
    """
    available_cameras = []
    camera_names = {
        0: "Cam-A",
        1: "Cam-B",
        2: "Cam-C",
        3: "Cam-D"
    }

    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_name = camera_names.get(i, f"camera {i}")
            available_cameras[i] = camera_name
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


def get_project_name():
    project_name = v.get_string('Please name the project: ')
    return project_name


def project_folders(project_name):
    """
    Creates project folders and picture storage from the cameras.
    :param project_name:
    :return:
    """
    # makes project folder
    project_folder = project_name.replace(" ", "_")
    os.makedirs(project_folder, exist_ok=True)

    # makes photos folder inside the project folder
    for i in range(4):
        photos_folder = os.path.join(project_folder, f"photos {i + 1}")
        os.makedirs(photos_folder, exist_ok=True)

    print("Project folders made.")


def focus_check():
    in_frame = v.get_y_or_n('Is everything in focus and in frame? (Y/N): ')
    return in_frame


def start_capture():
    start_cap = v.get_y_or_n('Ready to start? (Y/N): ')
    return start_cap


main()
