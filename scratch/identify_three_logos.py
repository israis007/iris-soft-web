import os
from PIL import Image

src_dir = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64'
new_files = [
    'media__1782183299680.png',
    'media__1782183299730.png',
    'media__1782183309827.png'
]

for filename in new_files:
    path = os.path.join(src_dir, filename)
    if os.path.exists(path):
        img = Image.open(path)
        print(f"File: {filename} | Format: {img.format} | Size: {img.size} | Mode: {img.mode}")
        
        # Look at pixel colors
        img_rgba = img.convert('RGBA')
        pixels = img_rgba.load()
        width, height = img_rgba.size
        
        # Sample non-white, non-transparent colors
        sample_colors = []
        for x in range(0, width, max(1, width // 50)):
            for y in range(0, height, max(1, height // 50)):
                r, g, b, a = pixels[x, y]
                if a > 100 and not (r > 240 and g > 240 and b > 240) and not (r < 15 and g < 15 and b < 15):
                    sample_colors.append((r, g, b))
        
        if sample_colors:
            avg_r = sum(c[0] for c in sample_colors) // len(sample_colors)
            avg_g = sum(c[1] for c in sample_colors) // len(sample_colors)
            avg_b = sum(c[2] for c in sample_colors) // len(sample_colors)
            print(f"  Avg Color: ({avg_r}, {avg_g}, {avg_b}) | Sample Count: {len(sample_colors)}")
    else:
        print("Not found:", path)
