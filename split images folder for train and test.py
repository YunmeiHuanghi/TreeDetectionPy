
def split_image_folder_train_test(train_ratio,input_folder,output_folder):
    # Define the split ratio
    train_ratio = train_ratio  # 80% for training, 20% for testing
    # Get the list of subdirectories (categories) within the input folder
    subdirectories = [subdir for subdir in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, subdir))]

    # Create the output directory structure
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'test'), exist_ok=True)
    #os.makedirs(os.path.join(output_folder, 'val'), exist_ok=True)

    # Loop through each subdirectory and split the images
    for subdir in subdirectories:
        subdirectory_path = os.path.join(input_folder, subdir)
        images = [image for image in os.listdir(subdirectory_path) if image.endswith('.jpg') or image.endswith('.png')]

        random.shuffle(images)
        num_train = int(len(images) * train_ratio)
        train_images = images[:num_train]
        test_images = images[num_train:]

        train_output_path = os.path.join(output_folder, 'train', subdir)
        test_output_path = os.path.join(output_folder, 'test', subdir)
        #test_output_path = os.path.join(output_folder, 'val', subdir)
 
        os.makedirs(train_output_path, exist_ok=True)
        os.makedirs(test_output_path, exist_ok=True)

        for image in train_images:
            source_path = os.path.join(subdirectory_path, image)
            destination_path = os.path.join(train_output_path, image)
            shutil.copy(source_path, destination_path)
            #print(source_path, destination_path)
        for image in test_images:
            source_path = os.path.join(subdirectory_path, image)
            destination_path = os.path.join(test_output_path, image)
            shutil.copy(source_path, destination_path)
            #print(source_path, '--->',destination_path)



# Usage example:
train_ratio = 0.8  # 80% for training, 20% for testing
input_folder = '/path/to/your/images'
output_folder = '/path/to/save/split/dataset'
split_image_folder_train_test(train_ratio, input_folder, output_folder)
This function doesn't need to return anything since it operates directly on the file system, creating directories and copying files. You can call the function with your desired train_ratio, input_folder, and output_folder to perform the train-test split for your image dataset.
#if you need add val folder, it's similar to these code.




