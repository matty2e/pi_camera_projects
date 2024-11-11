# ***************************************************************
# Author: Matt Tuohy
# Date: 11/2/2024
# Description: Tests connectivity, focus and position of cameras.
# Input: strings, integers
# Output: Photos, video and information about media
# Sources: realpython.com, collaboration on github
# ***************************************************************

# test run

# Welcome to Matt's PiCam test!
# Use this program to ensure the camera's being used are in focus, aligned
# properly, the lighting is good and the export settings are correct

# Where would you like to start?
# 1. How many cameras are connected?
# 2. Are they in focus and in the right position?
# 3. Where are the photos/videos being saved to?
# 4. Run capture test!
# 5. Start a new timelapse project.


# start
import valid as v
import cv2
import os
import glob


def main():
    # variables:
    choice_num = 0
    in_focus = str

    available_cameras = list_cameras()
    print("Welcome to the camera tester!\nCheck your cameras before "
          "timelapse.\n")
    display_menu()
    menu_choice = get_menu_choice()
    menu_execute_action(menu_choice)

    # calculations:

    # Output: Photos, strings of dialogue


# functions:
def display_menu():
    """
    Menu items list
    :return: none
    """
    print("Where would you like to start?:"
          "\n1. How many cameras are connected?"
          "\n2. Are they in focus and in the right position?"
          "\n3. Where are the photos/videos being saved to?"
          "\n4. Run capture test!")


def get_menu_choice():
    """
    Gets the integer for the menu choice.
    :return: int, menu choice
    """
    return v.get_integer("\nEnter your choice (1-4): ")


def menu_execute_action(menu_choice):
    """
    The action from the menu input that directs to the function needed to
    check the cameras connected to the PI.
    :param menu_choice: int, from the menu choice function
    :return: runs function selected from menu.
    """
    if menu_choice == 1:
        check_num_cameras()
    elif menu_choice == 2:
        check_focus()
    elif menu_choice == 3:
        check_save_locale()
    elif menu_choice == 4:
        run_capture_test()
    else:
        print("Try again")


# STOPPED HERE! Working on the camera check code

def check_num_cameras():
    """
    Checks the number of Arducam 5MP autofocus cameras connected to the Raspberry Pi.
    :return: string, number of cameras detected
    """
    # Check for the presence of the Arducam camera device files
    camera_files = glob.glob('/dev/video*')
    num_cameras = len(camera_files)

    # Determine the appropriate string output
    if num_cameras == 0:
        return "No cameras detected."
    elif num_cameras == 1:
        return "1 camera detected."
    else:
        return f"{num_cameras} cameras detected."


def check_focus(available_cameras):
    for i, camera_name in enumerate(available_cameras):
        print(f"checking focus for {camera_name}")
        cap = cv2.VideoCapture(i)

        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)

        focus_value = cap.get(cv2.CAP_PROP_FOCUS)
        print(f"Current focus value: {focus_value}")

        cap.set(cv2.CAP_PROP_FOCUS, focus_value + 10)
        new_focus_value = cap.get(cv2.CAP_PROP_FOCUS)
        print(f"New focus value: {new_focus_value}")

        cap.release()

    print("Camera focus check complete.")


def check_save_locale():
    print("You are saving to the computer")


def run_capture_test(available_cameras):
    for i, camera_name in enumerate(available_cameras):
        print(f"Capturing image from {camera_name} ...")
        cap = cv2.VideoCapture(i)
        ret, frame = cap.read()
        if ret:
            cv2.imshow(camera_name, frame)
            cv2.waitKey(3000)
        cap.release()

    print("camera test complete")


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


main()
