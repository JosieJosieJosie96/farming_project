import os
from PIL import Image

# Path to your downloaded images folder
cotton_folder = os.path.join("..", "data", "raw", "Cotton")

# List all files in the folder
img_files = os.listdir(cotton_folder)

# Open and show the first image
img_path = os.path.join(cotton_folder, img_files[0])
img = Image.open(img_path)
img.show()
