import os
import cv2

def apply_grayscale_filter(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over the files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an image
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Read the image
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Write the grayscale image to the output directory
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, gray_image)

            print(f"Processed image: {filename}")

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the input and output directories relative to the script's location
input_directory = os.path.join(script_dir, 'input')
output_directory = os.path.join(script_dir, 'output')

# Apply the grayscale filter to the images
apply_grayscale_filter(input_directory, output_directory)
