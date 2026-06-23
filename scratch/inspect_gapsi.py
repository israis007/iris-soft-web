import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782140309653.png'
if not os.path.exists(src):
    print("File not found:", src)
else:
    img = Image.open(src)
    print("Format:", img.format)
    print("Mode:", img.mode)
    print("Size:", img.size)
    
    # Check pixels
    pixels = img.convert('RGBA').getdata()
    transparent_count = sum(1 for p in pixels if p[3] == 0)
    semi_transparent_count = sum(1 for p in pixels if 0 < p[3] < 255)
    opaque_count = sum(1 for p in pixels if p[3] == 255)
    print(f"Transparent pixels: {transparent_count}")
    print(f"Semi-transparent pixels: {semi_transparent_count}")
    print(f"Opaque pixels: {opaque_count}")
