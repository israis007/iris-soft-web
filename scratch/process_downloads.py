import os
import shutil
from PIL import Image, ImageDraw

download_dir = r'C:\Users\mc_dj\Downloads'
dest_dir = r'c:\Users\mc_dj\AndroidStudioProjects\iris-soft-web\resources\logos'

os.makedirs(dest_dir, exist_ok=True)

# Helper function to upscale and remove outer white background using flood fill
def process_logo(src_filename, dest_filename, upscale_target=800, white_threshold=240, tolerance=20):
    src_path = os.path.join(download_dir, src_filename)
    dest_path = os.path.join(dest_dir, dest_filename)
    
    if not os.path.exists(src_path):
        print(f"[-] Source file not found: {src_filename}")
        return False
        
    print(f"[+] Processing {src_filename} -> {dest_filename}")
    img = Image.open(src_path).convert('RGBA')
    width, height = img.size
    
    # 1. Upscale if smaller than target resolution
    max_dim = max(width, height)
    if max_dim < upscale_target:
        scale_factor = upscale_target / max_dim
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        print(f"    Upscaling from {width}x{height} to {new_width}x{new_height}")
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        width, height = img.size
        
    # 2. Flood fill outer background starting from corners
    pixels = img.load()
    visited = [[False for _ in range(height)] for _ in range(width)]
    
    def is_white(r, g, b, a):
        # If already transparent, treat as visited background
        if a < 50:
            return True
        return r >= white_threshold and g >= white_threshold and b >= white_threshold
        
    queue = []
    # Add borders to queue
    for x in range(width):
        r, g, b, a = pixels[x, 0]
        if is_white(r, g, b, a):
            queue.append((x, 0))
            visited[x][0] = True
            
        r2, g2, b2, a2 = pixels[x, height - 1]
        if is_white(r2, g2, b2, a2):
            queue.append((x, height - 1))
            visited[x][height - 1] = True
            
    for y in range(height):
        r, g, b, a = pixels[0, y]
        if is_white(r, g, b, a):
            queue.append((0, y))
            visited[0][y] = True
            
        r2, g2, b2, a2 = pixels[width - 1, y]
        if is_white(r2, g2, b2, a2):
            queue.append((width - 1, y))
            visited[width - 1][y] = True
            
    # Directions for 4-connectivity flood fill
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    cleared_count = 0
    while queue:
        cx, cy = queue.pop(0)
        # Clear background pixel
        pixels[cx, cy] = (0, 0, 0, 0)
        cleared_count += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not visited[nx][ny]:
                    r, g, b, a = pixels[nx, ny]
                    # Check if pixel color is within tolerance of white
                    # Allow slight gradient/tolerance for anti-aliasing near borders
                    if a < 50 or (r >= (white_threshold - tolerance) and 
                                  g >= (white_threshold - tolerance) and 
                                  b >= (white_threshold - tolerance)):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        
    print(f"    Cleared {cleared_count} background pixels.")
    img.save(dest_path, 'WEBP', quality=95)
    print(f"    Saved transparent logo to: {dest_path}")
    return True

# --- Processing Tasks ---

# 1. Copy IDS directly
ids_src = os.path.join(download_dir, 'ids.webp')
ids_dest = os.path.join(dest_dir, 'ids.webp')
if os.path.exists(ids_src):
    shutil.copy(ids_src, ids_dest)
    print(f"[+] Copied IDS directly to {ids_dest}")
else:
    print("[-] IDS logo not found in Downloads!")

# 2. Convert Zeus (already transparent)
zeus_src = os.path.join(download_dir, 'ChatGPT Image 22 jun 2026, 12_42_31 p.m..png')
zeus_dest = os.path.join(dest_dir, 'zeuz.webp')
if os.path.exists(zeus_src):
    print(f"[+] Converting Zeus -> {zeus_dest}")
    img = Image.open(zeus_src).convert('RGBA')
    img.save(zeus_dest, 'WEBP', quality=95)
else:
    print("[-] Zeus logo not found in Downloads!")

# 3. Round Tecnoalfa corners (retaining abstract background)
tecnoalfa_src = os.path.join(download_dir, 'Gemini_Generated_Image_tgxspztgxspztgxs.png')
tecnoalfa_dest = os.path.join(dest_dir, 'tecnoalfa.webp')
if os.path.exists(tecnoalfa_src):
    print(f"[+] Converting & Rounding Tecnoalfa -> {tecnoalfa_dest}")
    img = Image.open(tecnoalfa_src).convert('RGBA')
    width, height = img.size
    
    # Create a rounded corner mask
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    # Apply a nice rounding radius (~60px for this size)
    draw.rounded_rectangle((0, 0, width, height), radius=60, fill=255)
    
    # Apply mask to image alpha channel
    img.putalpha(mask)
    img.save(tecnoalfa_dest, 'WEBP', quality=95)
else:
    print("[-] Tecnoalfa logo not found in Downloads!")

# 4. Process all other logos with background removal and scaling
process_logo('everis.png', 'everis.webp')
process_logo('consubanco.png', 'consubanco.webp')
process_logo('factumex.png', 'factumex.webp')
process_logo('MC1.png', 'mc1.webp')
process_logo('GLOBAL-HITSS.webp', 'globalhits.webp') # convert hitss to transparent webp
process_logo('ikusmen.jpg', 'ikusmen.webp')
process_logo('mtp.png', 'mtp.webp')
process_logo('AgileThought_Logo.jpg', 'agilethought.webp')
process_logo('flash-mobile-logo-png_seeklogo-378136.png', 'flashmobile.webp')
process_logo('logo_teambits.png', 'teambits.webp')
process_logo('satoritech.png', 'satoritech.webp')

print("\n[!] All logo tasks completed!")
