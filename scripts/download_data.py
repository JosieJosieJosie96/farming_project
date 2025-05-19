import kagglehub
from kagglehub import KaggleDatasetAdapter

# If you want to load the main dataset file (usually a CSV), just pass "" or omit file_path
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "aman2000jaiswal/agriculture-crop-images",
    "Crop_details.csv"
)

print("First 5 records:")
print(df.head())
