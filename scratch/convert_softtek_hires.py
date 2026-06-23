import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782112712112.png'
dest = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/softtek.webp'

img = Image.open(src).convert('RGBA')
width, height = img.size
pixels = img.load()

def is_bg_color(r, g, b):
    # Matches the light grey and white checkerboard pattern
    if r > 175 and g > 175 and b > 175:
        if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
            return True
    return False

cleared_count = 0
for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        if is_bg_color(r, g, b):
            pixels[x, y] = (0, 0, 0, 0)
            cleared_count += 1

print(f"Cleared {cleared_count} checkerboard pixels out of {width * height} total.")

# Save optimized WEBP
img.save(dest, 'WEBP', quality=95)
print("Successfully saved high-resolution transparent Softtek logo to WebP!")
