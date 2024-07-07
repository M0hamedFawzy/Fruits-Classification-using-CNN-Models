import os
from sklearn.model_selection import train_test_split
import shutil

def create_class_subdirectories(base_directory, classes):
    for class_name in classes:
        class_path = os.path.join(base_directory, class_name)
        os.makedirs(class_path, exist_ok=True)

# Path to the directory containing class folders
train_dir = r'D:\GP\Datasets\apical_ds_train_valid_test\validation+test'

# Path to the directory where you want to create train and validation sets
output_dir = r'D:\GP\Datasets\apical_ds_train_valid_test'

# List to store paths to all image files
image_paths = []

# Iterate through class folders
for class_folder in os.listdir(train_dir):
    class_path = os.path.join(train_dir, class_folder)
    # Add paths to all image files in the class folder
    image_paths.extend([os.path.join(class_path, img) for img in os.listdir(class_path)])

# Use train_test_split to get training and validation sets
train_paths, val_paths = train_test_split(image_paths, test_size=0.5, random_state=42)

# Create directories for train and validation sets
train_output_dir = os.path.join(output_dir, 'validation')
val_output_dir = os.path.join(output_dir, 'test')

# Create subdirectories for each class in train and validation sets
create_class_subdirectories(train_output_dir, os.listdir(train_dir))
create_class_subdirectories(val_output_dir, os.listdir(train_dir))

# Copy files to train and validation directories
for path in train_paths:
    class_name = os.path.basename(os.path.dirname(path))
    shutil.copy(path, os.path.join(train_output_dir, class_name, os.path.basename(path)))

for path in val_paths:
    class_name = os.path.basename(os.path.dirname(path))
    shutil.copy(path, os.path.join(val_output_dir, class_name, os.path.basename(path)))
