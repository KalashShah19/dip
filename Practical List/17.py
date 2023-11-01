#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:16:43 2023

@author: bmiit202006100110040
"""

import cv2

# Load the image
image = cv2.imread('input.jpg')

# Define the kernel size for median filtering
kernel_size = 3  # Adjust this size as needed

# Apply median filtering
median_filtered_image = cv2.medianBlur(image, kernel_size)

# Display the original and median-filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Median Filtered Image', median_filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
