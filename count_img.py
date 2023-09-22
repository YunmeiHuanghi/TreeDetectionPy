import os
import glob

# Define the folder path
folder_path = "/data/huan1643/bark_images/yolo_data_tree_id/val/images"
def check_number_img(folder_path):
    # Define a list of image extensions
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp"]
    
    # Initialize a variable to count the images
    image_count = 0
    
    # Loop through each image extension and count the matching files
    for ext in image_extensions:
        image_count += len(glob.glob(os.path.join(folder_path, ext)))
    # Print the total count of images
    print(f"Total number of images in {folder_path}: {image_count}")
check_number_img(folder_path)
