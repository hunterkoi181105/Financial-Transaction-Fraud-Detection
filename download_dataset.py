import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("aryan208/financial-transactions-dataset-for-fraud-detection")
print("Downloaded to:", path)

# Create destination directory if it doesn't exist
dest = os.getcwd() + "/dataset/"
os.makedirs(dest, exist_ok=True)


# Copy to desired location
shutil.copytree(path, dest, dirs_exist_ok=True)