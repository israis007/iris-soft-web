import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782140309653.png'
dest = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/gapsi.webp'

if not os.path.exists(src):
    print("Source file not found:", src)
else:
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    
    img = Image.open(src).convert('RGBA')
    img.save(dest, 'WEBP', quality=95)
    print("Successfully converted Gapsi logo to WebP and saved it at:", dest)
