#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:04:40 2023

@author: bmiit202006100110040
"""

import cv2

# Load the grayscale image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Set the threshold value to separate the objects of interest
threshold_value = 128  # Adjust this value as needed

# Perform intensity slicing with the background
_, object_mask = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Invert the object mask to obtain the background mask
background_mask = 255 - object_mask

# Apply the masks to obtain the objects of interest and the background
object_image = cv2.bitwise_and(image, image, mask=object_mask)
background_image = cv2.bitwise_and(image, image, mask=background_mask)

# Display the images
cv2.imshow('Objects of Interest', object_image)
cv2.imshow('Background', background_image)

cv2.waitKey(0)
cv2.destroyAllWindows()