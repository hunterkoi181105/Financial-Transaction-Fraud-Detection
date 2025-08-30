import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("aryan208/financial-transactions-dataset-for-fraud-detection")
print("Downloaded to:", path)
os.mkdir("dataset", exist_ok=True)
dest = os.getcwd() + "/dataset/"

# Move to desired location
os.rename(path, dest)