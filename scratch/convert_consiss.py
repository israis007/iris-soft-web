import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782140412673.png'
dest = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/consiss.webp'

if not os.path.exists(src):
    print("Source file not found:", src)
else:
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    
    img = Image.open(src).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
    cleared_count = 0
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            # If the pixel is near-white, make it transparent
            if r > 240 and g > 240 and b > 240:
                pixels[x, y] = (0, 0, 0, 0)
                cleared_count += 1
                
    img.save(dest, 'WEBP', quality=95)
    print(f"Cleared {cleared_count} white background pixels out of {width * height}.")
    print("Successfully saved transparent Consiss logo to WebP at:", dest)
