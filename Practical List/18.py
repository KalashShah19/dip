#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:18:00 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel size for min and max filtering
kernel_size = 3  # Adjust this size as needed

# Apply min filtering
min_filtered_image = cv2.erode(image, np.ones((kernel_size, kernel_size), np.uint8))

# Apply max filtering
max_filtered_image = cv2.dilate(image, np.ones((kernel_size, kernel_size), np.uint8))

# Display the original, min-filtered, and max-filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Min Filtered Image', min_filtered_image)
cv2.imshow('Max Filtered Image', max_filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
