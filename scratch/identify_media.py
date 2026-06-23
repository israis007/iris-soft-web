import os
from PIL import Image

src_dir = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64'
new_files = [
    'media__1782167492788.png',
    'media__1782167492820.png',
    'media__1782167492847.png'
]

for filename in new_files:
    path = os.path.join(src_dir, filename)
    if os.path.exists(path):
        img = Image.open(path)
        print(f"File: {filename} | Format: {img.format} | Size: {img.size} | Mode: {img.mode}")
        
        # Analyze colors of non-transparent pixels
        pixels = img.convert('RGBA').load()
        width, height = img.size
        sample_colors = []
        for x in range(0, width, 10):
            for y in range(0, height, 10):
                r, g, b, a = pixels[x, y]
                if a > 100:
                    sample_colors.append((r, g, b))
                    
        if sample_colors:
            avg_r = sum(c[0] for c in sample_colors) // len(sample_colors)
            avg_g = sum(c[1] for c in sample_colors) // len(sample_colors)
            avg_b = sum(c[2] for c in sample_colors) // len(sample_colors)
            print(f"  Avg Color: ({avg_r}, {avg_g}, {avg_b}) | Sample Count: {len(sample_colors)}")
            
            # Check signatures
            green_count = sum(1 for r, g, b in sample_colors if g > 150 and r < 100 and b < 100)
            purple_count = sum(1 for r, g, b in sample_colors if r > 100 and g < 100 and b > 100)
            cyan_count = sum(1 for r, g, b in sample_colors if r < 100 and g > 120 and b > 150)
            print(f"  Signatures -> Greenish: {green_count}, Purplish: {purple_count}, Cyanish: {cyan_count}")
    else:
        print("Not found:", path)
