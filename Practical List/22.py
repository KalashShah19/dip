import cv2
import numpy as np

# Load the binary image of an English alphabet
image = cv2.imread('alphabet_binary_image.png', cv2.IMREAD_GRAYSCALE)

# Define a kernel for the morphological operations
kernel = np.ones((3, 3), np.uint8)

# Erosion to obtain the external boundary
external_boundary = cv2.erode(image, kernel, iterations=1)

# Invert the image
inverted_image = 255 - image

# Dilation on the inverted image to obtain the internal boundary
internal_boundary = cv2.dilate(inverted_image, kernel, iterations=1)

# Perform logical AND between the internal boundary and the original image
internal_boundary = cv2.bitwise_and(image, internal_boundary)

# Display the original image, external boundary, and internal boundary
cv2.imshow('Original Image', image)
cv2.imshow('External Boundary', external_boundary)
cv2.imshow('Internal Boundary', internal_boundary)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
