import os
from PIL import Image

src_dir = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64'
dest_dir = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos'

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# 1. Process Consiss (Needs background removal)
consiss_src = os.path.join(src_dir, 'media__1782143021602.jpg')
consiss_dest = os.path.join(dest_dir, 'consiss.webp')

if os.path.exists(consiss_src):
    img = Image.open(consiss_src).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
    cleared_count = 0
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            # Background detection:
            # - Not extremely dark (to preserve black text/logos)
            # - Very low color saturation (R, G, B are very close because it's a grey-white gradient)
            max_val = max(r, g, b)
            min_val = min(r, g, b)
            diff = max_val - min_val
            
            if max_val > 65 and diff < 20:
                pixels[x, y] = (0, 0, 0, 0)
                cleared_count += 1
                
    img.save(consiss_dest, 'WEBP', quality=95)
    print(f"Consiss: Cleared {cleared_count} background pixels. Saved to {consiss_dest}")
else:
    print("Consiss source not found!")

# 2. Process Axity (Already transparent)
axity_src = os.path.join(src_dir, 'media__1782143073985.png')
axity_dest = os.path.join(dest_dir, 'axity.webp')
if os.path.exists(axity_src):
    img = Image.open(axity_src).convert('RGBA')
    img.save(axity_dest, 'WEBP', quality=95)
    print(f"Axity: Converted to WebP. Saved to {axity_dest}")
else:
    print("Axity source not found!")

# 3. Process TeamBits (Already transparent)
teambits_src = os.path.join(src_dir, 'media__1782143074027.png')
teambits_dest = os.path.join(dest_dir, 'teambits.webp')
if os.path.exists(teambits_src):
    img = Image.open(teambits_src).convert('RGBA')
    img.save(teambits_dest, 'WEBP', quality=95)
    print(f"TeamBits: Converted to WebP. Saved to {teambits_dest}")
else:
    print("TeamBits source not found!")

# 4. Process SatoriTech (Already transparent)
satoritech_src = os.path.join(src_dir, 'media__1782143074037.png')
satoritech_dest = os.path.join(dest_dir, 'satoritech.webp')
if os.path.exists(satoritech_src):
    img = Image.open(satoritech_src).convert('RGBA')
    img.save(satoritech_dest, 'WEBP', quality=95)
    print(f"SatoriTech: Converted to WebP. Saved to {satoritech_dest}")
else:
    print("SatoriTech source not found!")
