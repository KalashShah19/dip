#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:48:27 2023

@author: Kalash Shah
"""
import cv2
import numpy as np

image = cv2.imread('4.jpg', 0)

_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#binary_image = cv2.bitwise_not(binary_image)
kernel=np.ones((3,3),np.uint8)

#erosion
binary_image = cv2.erode(binary_image, kernel, iterations=1) 

# Apply component labeling
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=8)

# Create a random color map for labeling visualization
color_map = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)

# Create an output image for visualization
output_image = np.zeros((binary_image.shape[0], binary_image.shape[1], 3), dtype=np.uint8)

# Visualize labeled components
for label in range(1, num_labels):
    output_image[labels == label] = color_map[label]

res = num_labels - 1;
out = "Labeled Image, Stars = " + str(res)

# Display the labeled image
cv2.imshow('Binary Image', image)
cv2.imshow(out, output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the number of labels (excluding background label 0)
print("Number of labels:" , num_labels - 1)