"""Downloads the dashboard images the first time the app is prepared.
Run: python download_images.py
If a network is unavailable, the website still works with its CSS placeholders.
"""
from pathlib import Path
from urllib.request import Request, urlopen

OUT = Path(__file__).parent / "static" / "images"
OUT.mkdir(parents=True, exist_ok=True)
IMAGES = {
    "campus.jpg": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80",
    "library.jpg": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=900&q=80",
    "classroom.jpg": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=80",
    "student.jpg": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=900&q=80",
}
for filename, url in IMAGES.items():
    target = OUT / filename
    if target.exists() and target.stat().st_size > 5000:
        print(f"Already downloaded: {filename}")
        continue
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=20) as response:
            data = response.read()
        if len(data) < 5000:
            raise ValueError("Downloaded file is unexpectedly small")
        target.write_bytes(data)
        print(f"Downloaded: {filename}")
    except Exception as exc:
        print(f"Could not download {filename}: {exc}")
print("Image setup finished. The app also works if image downloads are unavailable.")
