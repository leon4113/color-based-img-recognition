import cv2
import numpy as np
from typing import List

def find_objects_by_color(image: np.ndarray) -> List[np.ndarray]:
    """
    Finds objects in an image based on automatic color thresholding using Gaussian neighborhood.

    Parameters:
        image (np.ndarray): The input image in BGR color space.

    Returns:
        List[np.ndarray]: A list of contours representing the detected objects.

    """
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    """
    threshold for yellow color (Hue range 20-40)
    lower_yellow = np.array([20, 100, 100])  
    upper_yellow = np.array([40, 255, 255])
    
    Create a mask for the yellow color
    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    """

    # Set the lower and upper color thresholds for red color (apple)
    lower_red1 = np.array([0, 100, 100])  # threshold for red color (Hue range 0-10)
    upper_red1 = np.array([10, 255, 255])
    # 2 thresold because red color range for hue is 0-10 and 160-179
    #threshold for red color (Hue range 160-179)
    lower_red2 = np.array([160, 100, 100])  
    upper_red2 = np.array([179, 255, 255])  

    # Create a mask for the red color
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask = mask1 + mask2  # Combine masks for both hue ranges

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# Load and resize the image
image = cv2.imread('sample.jpeg')
image = cv2.resize(image, (400, 640))  # Resize the image

objects = find_objects_by_color(image)

# Draw bounding rectangles around the detected objects
min_area_threshold = 500  # Minimum area threshold for filtering out small contours

for contour in objects:
    if cv2.contourArea(contour) > min_area_threshold:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
