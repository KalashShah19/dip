#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:18:11 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Laplacian filter for edge detection
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

# Convert the Laplacian result back to 8-bit image
laplacian = np.uint8(np.absolute(laplacian))

# Add the Laplacian result to the original image to perform sharpening
sharpened_image = cv2.addWeighted(image, 1.5, cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR), -0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
