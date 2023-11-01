#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:06:17 2023

@author: bmiit202006100110040
"""

import cv2

# Load the grayscale image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Thresholding based on the middle value
middle_value_threshold, middle_value_binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Thresholding based on the average pixel value
average_pixel_value = int(image.mean())
average_threshold, average_threshold_binary = cv2.threshold(image, average_pixel_value, 255, cv2.THRESH_BINARY)

# Thresholding using Otsu's method
_, otsu_threshold_binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original image and the binary images
cv2.imshow('Original Image', image)
cv2.imshow('Middle Value Threshold Binary', middle_value_binary)
cv2.imshow('Average Threshold Binary', average_threshold_binary)
cv2.imshow("Otsu's Threshold Binary", otsu_threshold_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
