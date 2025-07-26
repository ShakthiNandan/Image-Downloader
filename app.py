import os
import re
import requests
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import jsonify
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Google Custom Search settings
API_KEY = os.getenv("API_KEY")
CSE_ID = os.getenv("CSE_ID")
SEARCH_URL = "https://www.googleapis.com/customsearch/v1"

download_folder = Path("static/downloads")
download_folder.mkdir(parents=True, exist_ok=True)

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', name) + ".jpg"

def search_images(query):
    params = {
        'key': API_KEY,
        'cx': CSE_ID,
        'q': query,
        'searchType': 'image',
        'num': 8
    }
    response = requests.get(SEARCH_URL, params=params)
    if response.status_code == 200:
        return [item['link'] for item in response.json().get('items', [])]
    return []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        images = search_images(query)
        return render_template("results.html", query=query, images=images)
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")
    name = sanitize_filename(data.get("name", "image"))

    try:
        response = requests.get(url)
        response.raise_for_status()
        path = download_folder / name
        with open(path, "wb") as f:
            f.write(response.content)
        return jsonify({"status": "success", "message": f"{name} downloaded."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
