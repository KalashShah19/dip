import cv2

# Load the grayscale image
image = cv2.imread('grayscale_image.jpg', cv2.IMREAD_GRAYSCALE)

# Adjust the brightness by adding a constant value
brightness_increase = 50  # Adjust this value as needed

# Increase the brightness by adding the constant value
brightened_image = image + brightness_increase

# Ensure pixel values remain within the valid range [0, 255]
brightened_image = cv2.normalize(brightened_image, None, 0, 255, cv2.NORM_MINMAX)

# Display the original and brightened images
cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Brightened Image', brightened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
