#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:10:01 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Define the 3x3 standard blurring kernel
kernel_3x3 = (1/9) * np.ones((3,3),np.uint8)

# Define the 7x7 standard blurring kernel
kernel_7x7 = (1/49) * np.ones((7,7),np.uint8)

# Apply 3x3 standard blurring three times
for _ in range(3):
    image = cv2.filter2D(image, -1, kernel_3x3)

# Apply 7x7 standard blurring
blurred_image_7x7 = cv2.filter2D(image, -1, kernel_7x7)

# Display the original, 3x3 blurred, and 7x7 blurred images
cv2.imshow('Original Image', image)
cv2.imshow('3x3 Blurred Image', image)
cv2.imshow('7x7 Blurred Image', blurred_image_7x7)

cv2.waitKey(0)
cv2.destroyAllWindows()
