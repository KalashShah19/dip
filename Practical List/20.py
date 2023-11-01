#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:19:13 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the kernel for blurring
kernel_size = 5
blur_kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.filter2D(gray_image, -1, blur_kernel)

# Calculate the difference (mask) between the original and blurred images
mask = gray_image - blurred_image

# Define a list of k values
k_values = [0.5, 1, 1.5]

# Apply unsharp masking for different k values
sharpened_images = []
for k in k_values:
    unsharp_image = gray_image + k * mask
    sharpened_images.append(unsharp_image)

# Display the original and sharpened images for different k values
cv2.imshow('Original Image', gray_image)
for i, k in enumerate(k_values):
    cv2.imshow(f'Sharpened Image (k={k})', sharpened_images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
