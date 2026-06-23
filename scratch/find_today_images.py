import os
import time

download_dir = r'C:\Users\mc_dj\Downloads'
image_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.heic', '.avif')

files = os.listdir(download_dir)
today_images = []

# June 22, 2026 timestamp range
# Let's just find anything modified on June 22, 2026 (local time)
for f in files:
    ext = os.path.splitext(f)[1].lower()
    if ext in image_extensions:
        path = os.path.join(download_dir, f)
        mtime = os.path.getmtime(path)
        lt = time.localtime(mtime)
        if lt.tm_year == 2026 and lt.tm_mon == 6 and lt.tm_mday == 22:
            today_images.append((f, mtime, os.path.getsize(path)))

today_images.sort(key=lambda x: x[1], reverse=True)

print(f"Total image files modified today: {len(today_images)}")
for f, mtime, size in today_images:
    local_time = time.strftime('%H:%M:%S', time.localtime(mtime))
    print(f" - {f} | Size: {size} bytes | Modified: {local_time}")
