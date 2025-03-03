from picamera2 import Picamera2
import numpy as np

def capture_and_analyze():
    # Initialize the camera
    picam2 = Picamera2()
    picam2.start()

    # Capture an image
    image = picam2.capture_array()

    # Convert to grayscale
    gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # Convert to grayscale using the luminosity method

    # Calculate the average brightness
    average_brightness = np.mean(gray_image)

    picam2.stop()
    return average_brightness

if __name__ == "__main__":
    brightness = capture_and_analyze()
    print(f'Average Brightness: {brightness}')
