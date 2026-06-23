import os
import time

download_dir = r'C:\Users\mc_dj\Downloads'

files = os.listdir(download_dir)
today_files = []

for f in files:
    path = os.path.join(download_dir, f)
    if os.path.isfile(path):
        mtime = os.path.getmtime(path)
        lt = time.localtime(mtime)
        if lt.tm_year == 2026 and lt.tm_mon == 6 and lt.tm_mday == 22:
            today_files.append((f, mtime, os.path.getsize(path)))

today_files.sort(key=lambda x: x[1], reverse=True)

print(f"Total files modified today in Downloads: {len(today_files)}")
for f, mtime, size in today_files:
    local_time = time.strftime('%H:%M:%S', time.localtime(mtime))
    print(f" - {f} | Size: {size} bytes | Modified: {local_time}")
