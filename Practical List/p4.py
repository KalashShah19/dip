import cv2

# Function to check pixel adjacency
def check_adjacency(image, pixel1, pixel2, adjacency_type):
    x1, y1 = pixel1
    x2, y2 = pixel2

    if adjacency_type == '4-adjacent':
        return abs(x1 - x2) + abs(y1 - y2) == 1

    if adjacency_type == '8-adjacent':
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

    if adjacency_type == 'm-adjacent':
        return abs(x1 - x2) <= 1 or abs(y1 - y2) <= 1

# Input a grayscale image (you can load it with cv2.imread)
image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Input two pixel positions (x, y) for testing
pixel1 = (1, 1)
pixel2 = (2, 1)

# Specify the adjacency type (choose one: '4-adjacent', '8-adjacent', 'm-adjacent')
adjacency_type = '4-adjacent'

# Check adjacency and display the result
result = check_adjacency(image, pixel1, pixel2, adjacency_type)

if result:
    print(f"The pixels {pixel1} and {pixel2} are {adjacency_type}.")
else:
    print(f"The pixels {pixel1} and {pixel2} are not {adjacency_type}.")
