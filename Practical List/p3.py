import cv2

# Load the grayscale image
image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Input the pixel position (x, y)
x = 50  # Adjust this to the desired x-coordinate
y = 50  # Adjust this to the desired y-coordinate

# Get the pixel value at the input position
center_value = image[y, x]

# Define 8 possible neighbor positions (4-neighbors, diagonal neighbors, and the center itself)
neighbors = [
    (x - 1, y), (x + 1, y),  # Left and right neighbors
    (x, y - 1), (x, y + 1),  # Top and bottom neighbors
    (x - 1, y - 1), (x + 1, y - 1),  # Diagonal neighbors
    (x - 1, y + 1), (x + 1, y + 1)
]

# Display the pixel positions and values of neighbors
print(f"Center Pixel ({x}, {y}) Value: {center_value}")

for i, (neighbor_x, neighbor_y) in enumerate(neighbors):
    if 0 <= neighbor_x < image.shape[1] and 0 <= neighbor_y < image.shape[0]:
        neighbor_value = image[neighbor_y, neighbor_x]
        print(f"Neighbor {i + 1} Pixel ({neighbor_x}, {neighbor_y}) Value: {neighbor_value}")
    else:
        print(f"Neighbor {i + 1} Pixel ({neighbor_x}, {neighbor_y}) is outside the image.")
