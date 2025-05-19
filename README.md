# Image Tagger- Farming Project


This project is a local image tagging tool for managing agricultural crop images. You can add and remove tags to individual images or whole folders and store metadata in MongoDB.


## 🚀 Features


- Tag images with predefined labels
- Save tags to a local file or database
- Designed for use in data pipelines or manual curation


📁 Project Structure


image-tagger/


├── app


    └── _init_.py


    └── main.py


    └── utils.py


├── data/


│   └── raw/


│       └── crop_images/          # Contains folders like wheat/, maize/, etc.


├── scripts/


    └── _init_.py


    └── database.py


    └── download_data.py


    └── process_images.py

└── README.md


└── requirements.txt


⚙️ Prerequisites


Python 3.10+

MongoDB (local or Atlas)

Kaggle account (for dataset download)

Dependencies:


pip install pymongo python-dotenv kagglehub pandas pytest

🧬 MongoDB Setup


Create a file called database.py:


from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "image_tagger"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]




MONGO_URI=mongodb://localhost:27017/
DB_NAME=image_tagger


