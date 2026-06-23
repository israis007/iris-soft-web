import os
import time

download_dir = r'C:\Users\mc_dj\Downloads'
image_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.heic', '.avif')

files = os.listdir(download_dir)
image_files_with_time = []

for f in files:
    ext = os.path.splitext(f)[1].lower()
    if ext in image_extensions:
        path = os.path.join(download_dir, f)
        mtime = os.path.getmtime(path)
        image_files_with_time.append((f, mtime, os.path.getsize(path)))

# Sort by modification time desc (newest first)
image_files_with_time.sort(key=lambda x: x[1], reverse=True)

print("Top 30 newest image files in Downloads:")
for f, mtime, size in image_files_with_time[:30]:
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
    print(f" - {f} | Size: {size} bytes | Modified: {local_time}")
