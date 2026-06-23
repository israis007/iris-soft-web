import os
import time
from PIL import Image

download_dir = r'C:\Users\mc_dj\Downloads'
image_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.heic', '.avif')

files = os.listdir(download_dir)
today_images = []

for f in files:
    ext = os.path.splitext(f)[1].lower()
    if ext in image_extensions:
        path = os.path.join(download_dir, f)
        mtime = os.path.getmtime(path)
        lt = time.localtime(mtime)
        if lt.tm_year == 2026 and lt.tm_mon == 6 and lt.tm_mday == 22:
            today_images.append((f, mtime, path))

today_images.sort(key=lambda x: x[1], reverse=True)

print(f"Inspecting {len(today_images)} images modified today:")
for f, mtime, path in today_images:
    try:
        img = Image.open(path)
        print(f"File: {f} | Size: {img.size} | Mode: {img.mode} | Format: {img.format}")
    except Exception as e:
        print(f"File: {f} | Error opening: {e}")
