import os
from PIL import Image

src_dir = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64'
dest_dir = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos'

def clean_and_convert(src_filename, dest_filename, white_threshold=240, tolerance=20):
    src_path = os.path.join(src_dir, src_filename)
    dest_path = os.path.join(dest_dir, dest_filename)
    
    if not os.path.exists(src_path):
        print(f"[-] Source file not found: {src_filename}")
        return False
        
    print(f"[+] Processing {src_filename} -> {dest_filename}")
    img = Image.open(src_path).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
    # Border-seeded flood fill to clear background
    visited = [[False for _ in range(height)] for _ in range(width)]
    
    def is_white(r, g, b, a):
        if a < 50:
            return True
        return r >= white_threshold and g >= white_threshold and b >= white_threshold
        
    queue = []
    # Add border pixels to queue
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
            
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cleared_count = 0
    
    while queue:
        cx, cy = queue.pop(0)
        pixels[cx, cy] = (0, 0, 0, 0)
        cleared_count += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not visited[nx][ny]:
                    r, g, b, a = pixels[nx, ny]
                    if a < 50 or (r >= (white_threshold - tolerance) and 
                                  g >= (white_threshold - tolerance) and 
                                  b >= (white_threshold - tolerance)):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        
    print(f"    Cleared {cleared_count} background pixels.")
    
    # Trim transparent borders using getbbox
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        print(f"    Cropped margins to: {img.size}")
        
    img.save(dest_path, 'WEBP', quality=95)
    print(f"    Saved to: {dest_path}")
    return True

# Process the three files
clean_and_convert('media__1782167492788.png', 'baz.webp')
clean_and_convert('media__1782167492820.png', 'flashmobile.webp')
clean_and_convert('media__1782167492847.png', 'mc1.webp')

print("\n[!] Processing complete!")
