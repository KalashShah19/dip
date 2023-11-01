import math

# Input the coordinates of two pixel positions (x1, y1) and (x2, y2)
x1, y1 = 10, 10  # Adjust these coordinates as needed
x2, y2 = 20, 20  # Adjust these coordinates as needed

# Calculate the Euclidean distance (De)
de_distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate the D4 distance (Manhattan distance)
d4_distance = abs(x1 - x2) + abs(y1 - y2)

# Calculate the D8 distance (Chebyshev distance)
d8_distance = max(abs(x1 - x2), abs(y1 - y2))

# Display the distances
print(f"Euclidean (De) Distance between ({x1}, {y1}) and ({x2}, {y2}): {de_distance}")
print(f"D4 Distance between ({x1}, {y1}) and ({x2}, {y2}): {d4_distance}")
print(f"D8 Distance between ({x1}, {y1}) and ({x2}, {y2): {d8_distance}")
