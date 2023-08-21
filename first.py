import cv2

img = cv2.imread("py.jpg",0)

height, width = img.shape[:-1]
resolution = "Image Resolution = " + str(height) + " x " + str(width)
cv2.imshow(resolution, img)

cv2.waitKey(0)

cv2.destroyAllWindows()