import typer
from PIL import Image
import subprocess
import json
from rich import print
from pathlib import Path
from pymongo import MongoClient

app = typer.Typer()
client = MongoClient("mongodb://localhost:27017/")
db = client["image_db"]
collection = db["metadata"]

def sanitize_keys(d):
    """Replace invalid MongoDB keys recursively."""
    if isinstance(d, dict):
        new_dict = {}
        for k, v in d.items():
            new_key = k.replace('.', '_').replace('$', '_')
            new_dict[new_key] = sanitize_keys(v)
        return new_dict
    elif isinstance(d, list):
        return [sanitize_keys(i) for i in d]
    else:
        return d

def extract_metadata(image_path: Path):
    result = subprocess.run(
    [r"C:\Users\waltr\Downloads\exiftool.exe\exiftool-13.29_32\exiftool.exe", "-j", str(image_path)],
    capture_output=True,
    text=True
)
    return json.loads(result.stdout)[0] if result.stdout else {}

@app.command()
def tag_image(path: Path, tag: str):
    """Tag an image and store metadata in MongoDB"""
    if not path.exists():
        print(f"[red]File {path} does not exist[/red]")
        return
    metadata = extract_metadata(path)
    metadata["tag"] = tag
    metadata["filename"] = path.name
    sanitized_metadata = sanitize_keys(metadata)
    collection.insert_one(sanitized_metadata)
    print(f"[green]Tagged {path.name} with '{tag}'[/green]")


@app.command()
def list_tags():
    """List all tags in the database"""
    tags = collection.distinct("tag")
    print(f"[cyan]Available tags: {tags}[/cyan]")

if __name__ == "__main__":
    app()


