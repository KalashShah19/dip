import cv2

def add_image_center(main_image_path, image_to_add_path, output_path):
    # Read the main image and image to be added
    main_image = cv2.imread(main_image_path)
    image_to_add = cv2.imread(image_to_add_path)

    if main_image is None or image_to_add is None:
        print("Error: Unable to read one or both of the images.")
        return

    # Get the dimensions of the main image and image to be added
    main_height, main_width, _ = main_image.shape
    add_height, add_width, _ = image_to_add.shape

    # Calculate the position to place the image at the center
    center_x = (main_width - add_width) // 2
    center_y = (main_height - add_height) // 2

    # Overlay the image at the center
    main_image[center_y:center_y+add_height, center_x:center_x+add_width] = image_to_add

    # Save the result
    cv2.imwrite(output_path, main_image)

    # Display the result (optional)
    cv2.imshow("Result", main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_image_path = "temp.jpg"
    image_to_add_path = "py.png"
    output_path = "new.jpg"
    add_image_center(main_image_path, image_to_add_path, output_path)
