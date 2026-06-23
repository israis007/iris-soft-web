import os
import urllib.request
import time
from PIL import Image, ImageDraw, ImageFont

dest_dir = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos'
os.makedirs(dest_dir, exist_ok=True)

# List of major brand logos to try downloading from Wikimedia Commons
downloads = {
    'liverpool': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Liverpool_logo.svg/500px-Liverpool_logo.svg.png',
    'oxxo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Oxxo_Logo.svg/500px-Oxxo_Logo.svg.png',
    'santander': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Banco_Santander_Logotipo.svg/500px-Banco_Santander_Logotipo.svg.png',
    'citibanamex': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Banamex.svg/500px-Banamex.svg.png',
    'pepsico': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/PepsiCo_logo.svg/500px-PepsiCo_logo.svg.png',
    'telcel': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Telcel_logo_2022.svg/500px-Telcel_logo_2022.svg.png',
    'italika': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Logo_de_Italika.svg/500px-Logo_de_Italika.svg.png',
    'everis': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Everis_logo.svg/500px-Everis_logo.svg.png'
}

# If any logo download fails, we fallback to a generated avatar
fallbacks = {
    'gapsi': ('GAPSI', '#0984e3', '#dfe6e9'),
    'spinfood': ('SPIN', '#00b894', '#ffeaa7'),
    'consiss': ('CONSISS', '#6c5ce7', '#a29bfe'),
    'mtp': ('MTP', '#00cec9', '#81ecec'),
    'satoritech': ('SATORI', '#d63031', '#ff7675'),
    'factumex': ('FACTUM', '#2d3436', '#dfe6e9'),
    'zeuz': ('ZEUZ', '#fdcb6e', '#ffeaa7'),
    'tecnoalfa': ('TECNO', '#e17055', '#ff7675'),
    'consubanco': ('CONSU', '#e84393', '#fd79a8'),
    'axity': ('AXITY', '#2c3e50', '#bdc3c7'),
    'mc1': ('MC1', '#27ae60', '#2ecc71'),
    'ikusmen': ('IKUS', '#8e44ad', '#9b59b6'),
    'teambits': ('BITS', '#f39c12', '#f1c40f'),
    'flashmobile': ('FLASH', '#c0392b', '#e74c3c'),
    'reddog': ('REDDOG', '#d35400', '#e67e22')
}

def is_white_or_checkerboard(r, g, b):
    # Matches white or light grey checkerboard cells
    if r > 180 and g > 180 and b > 180:
        if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
            return True
    return False

def remove_background(img_path):
    img = Image.open(img_path).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
    # Simple border-seeded flood fill
    visited = [[False for _ in range(height)] for _ in range(width)]
    queue = []
    
    for x in range(width):
        if is_white_or_checkerboard(*pixels[x, 0][:3]):
            queue.append((x, 0))
            visited[x][0] = True
        if is_white_or_checkerboard(*pixels[x, height - 1][:3]):
            queue.append((x, height - 1))
            visited[x][height - 1] = True
            
    for y in range(height):
        if is_white_or_checkerboard(*pixels[0, y][:3]):
            queue.append((0, y))
            visited[0][y] = True
        if is_white_or_checkerboard(*pixels[width - 1, y][:3]):
            queue.append((width - 1, y))
            visited[width - 1][y] = True
            
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.pop(0)
        pixels[x, y] = (0, 0, 0, 0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not visited[nx][ny]:
                    r, g, b, a = pixels[nx, ny]
                    if is_white_or_checkerboard(r, g, b):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        
    # Clean inner white holes (like in letters)
    for x in range(width):
        for y in range(height):
            if not visited[x][y]:
                r, g, b, a = pixels[x, y]
                if is_white_or_checkerboard(r, g, b):
                    pixels[x, y] = (0, 0, 0, 0)
                    
    img.save(img_path, 'WEBP', quality=95)

def generate_avatar(name, text, bg_color, fg_color):
    # Generates a clean typography-based avatar
    img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer circle/hexagon shape
    draw.ellipse([30, 30, 270, 270], fill=bg_color, outline='#ffffff', width=6)
    
    # Standard text drawing (default font since custom font might not be available)
    # Using simple layout calculation
    text_w = len(text) * 16
    draw.text((150 - text_w, 130), text, fill=fg_color, font=None, size=32)
    
    dest_path = os.path.join(dest_dir, f"{name}.webp")
    img.save(dest_path, 'WEBP', quality=95)
    print(f"Generated fallback avatar for {name}")

# Try to download major brands
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

for name, url in downloads.items():
    dest_path = os.path.join(dest_dir, f"{name}.webp")
    try:
        print(f"Waiting 3 seconds before downloading {name} logo...")
        time.sleep(3)
        print(f"Downloading {name} logo from {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response, open(dest_path, 'wb') as out_file:
            out_file.write(response.read())
        # Clean the background and save as transparent WebP
        remove_background(dest_path)
        print(f"Successfully processed {name} logo!")
    except Exception as e:
        print(f"Failed to download {name} logo: {e}. Generating fallback avatar...")
        fallback_text = name.upper()[:5]
        # Custom color codes for major brands
        color_map = {
            'liverpool': ('LVP', '#d63031', '#ffffff'),
            'oxxo': ('OXXO', '#e74c3c', '#f1c40f'),
            'santander': ('SAN', '#e74c3c', '#ffffff'),
            'citibanamex': ('BNMX', '#0984e3', '#ffffff'),
            'pepsico': ('PEP', '#0984e3', '#ffffff'),
            'telcel': ('TCL', '#0984e3', '#ffffff'),
            'italika': ('ITK', '#27ae60', '#f1c40f'),
            'everis': ('EVS', '#7f8c8d', '#2c3e50')
        }
        text, bg, fg = color_map.get(name, (fallback_text, '#2c3e50', '#ffffff'))
        generate_avatar(name, text, bg, fg)

# Generate other consulting avatars
for name, data in fallbacks.items():
    text, bg, fg = data
    generate_avatar(name, text, bg, fg)

print("\nAll logo assets processed successfully!")
