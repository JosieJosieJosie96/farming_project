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

def extract_metadata(image_path: Path):
    result = subprocess.run(["exiftool", "-j", str(image_path)], capture_output=True, text=True)
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
    collection.insert_one(metadata)
    print(f"[green]Tagged {path.name} with '{tag}'[/green]")

@app.command()
def list_tags():
    """List all tags in the database"""
    tags = collection.distinct("tag")
    print(f"[cyan]Available tags: {tags}[/cyan]")

if __name__ == "__main__":
    app()
