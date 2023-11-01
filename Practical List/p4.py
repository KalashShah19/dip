# Function to check pixel adjacency
def check_adjacency(pixel1, pixel2, adjacency_type):
    x1, y1 = pixel1
    x2, y2 = pixel2

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if adjacency_type == '4-adjacent':
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

    if adjacency_type == '8-adjacent':
        return dx <= 1 and dy <= 1

    if adjacency_type == 'm-adjacent':
        return dx <= 1 or dy <= 1

# Input a grayscale image (you can load it with cv2.imread)
# Assuming an image with a shape (height, width), where pixel positions are (x, y)
image = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

# Input two pixel positions (x, y) for testing
pixel1 = (1, 1)
pixel2 = (2, 1)

# Specify the adjacency type (choose one: '4-adjacent', '8-adjacent', 'm-adjacent')
adjacency_type = '4-adjacent'

# Check adjacency and display the result
result = check_adjacency(pixel1, pixel2, adjacency_type)

if result:
    print(f"The pixels {pixel1} and {pixel2} are {adjacency_type}.")
else:
    print(f"The pixels {pixel1} and {pixel2} are not {adjacency_type}.")
