import os
from PIL import Image

logos_dir = r'c:\Users\mc_dj\AndroidStudioProjects\iris-soft-web\resources\logos'
files = os.listdir(logos_dir)

print("Starting automatic transparent margin trimming for all logos...")

for f in files:
    if f.lower().endswith('.webp'):
        path = os.path.join(logos_dir, f)
        try:
            img = Image.open(path).convert('RGBA')
            bbox = img.getbbox()
            
            if bbox:
                # Calculate size before crop
                w_orig, h_orig = img.size
                cropped_img = img.crop(bbox)
                w_new, h_new = cropped_img.size
                
                # Only save if it actually trimmed something significant
                if w_new < w_orig or h_new < h_orig:
                    cropped_img.save(path, 'WEBP', quality=95)
                    print(f" [+] Trimmed {f}: {w_orig}x{h_orig} -> {w_new}x{h_new}")
                else:
                    print(f" [~] No trimming needed for {f}: {w_orig}x{h_orig}")
            else:
                print(f" [-] Image {f} is completely empty/transparent")
        except Exception as e:
            print(f" [!] Error processing {f}: {e}")

print("\nFinished trimming logo margins!")
