#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:24:00 2023

@author: bmiit202006100110040
"""

import cv2

def get_adjacent_neighbors(image, x, y, m):
    height, width = image.shape[:2]

    # Validate pixel coordinates
    if x < 0 or y < 0 or x >= width or y >= height:
        raise ValueError("Invalid pixel coordinates")

    # Define neighbor coordinates offsets
    neighbor_offsets = [
        (dx, dy) for dx in range(-m, m+1) for dy in range(-m, m+1) if (dx, dy) != (0, 0)
    ]

    neighbors = []
    for dx, dy in neighbor_offsets:
        neighbor_x = x + dx
        neighbor_y = y + dy

        # Check if the neighbor is within the image boundaries
        if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
            neighbors.append((neighbor_x, neighbor_y))

    return neighbors

# Load an image
image = cv2.imread('colors.jpg', 0)

# Define the pixel coordinates for which you want to find adjacent neighbors
pixel_x, pixel_y = 100, 100

# Define the 'm' value for the number of adjacent neighbors (including diagonals)
m = 1

# Get the adjacent neighbors of the pixel
adjacent_neighbors = get_adjacent_neighbors(image, pixel_x, pixel_y, m)

# Print the coordinates of the adjacent neighbors
print("Adjacent neighbors:")
for neighbor_x, neighbor_y in adjacent_neighbors:
    print(f"({neighbor_x}, {neighbor_y})")