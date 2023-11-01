import cv2

# Load the image
image = cv2.imread('image.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get image dimensions (resolution)
height, width = image.shape[:2]

# Determine image type (binary, grayscale, or color)
image_type = "Binary" if len(image.shape) == 2 else "Grayscale" if len(image.shape) == 3 and image.shape[2] == 1 else "Color"

# Display image resolution and type
print(f"Image Resolution: {width} x {height}")
print(f"Image Type: {image_type}")
