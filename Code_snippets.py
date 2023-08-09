from tqdm import tqdm 
import os
from glob import glob

source_dir ='Pignut_hickory/labels'
destination_dir ='Sugar_maple/labels'             

for root, dirs, files in os.walk(source_dir):
    for file in glob("Pignut_hickory/labels/*SM*"):
        file_name=os.path.basename(file)
        source_file_path = os.path.join(root, file_name)
        destination_file_path = os.path.join(destination_dir, file_name)
        # the distination file path is not correct, get the file base name to save is correct now.
        print(source_file_path,"-->",destination_file_path)
        shutil.move(source_file_path, destination_file_path)




## split data
!pip install split-folders 


#split folders into train/test 
import splitfolders
splitfolders.ratio('train_20211102', output="output_train_20211102", seed=1337, ratio=(.8,0.2)) 
