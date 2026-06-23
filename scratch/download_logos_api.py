import os
import time
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageDraw

dest_dir = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos'
os.makedirs(dest_dir, exist_ok=True)

# Wikimedia file names to query via API
queries = {
    'liverpool': 'File:Liverpool logo.svg',
    'oxxo': 'File:Oxxo Logo.svg',
    'santander': 'File:Banco Santander Logotipo.svg',
    'citibanamex': 'File:Banamex.svg',
    'pepsico': 'File:PepsiCo logo.svg',
    'telcel': 'File:Telcel logo 2022.svg',
    'italika': 'File:Logo de Italika.svg',
    'everis': 'File:Everis logo.svg'
}

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
    'reddog': ('REDDOG', '#d35400', '#e67e22'),
    'agilethought': ('AGILE', '#1abc9c', '#ffffff'),
    'ids': ('IDS', '#34495e', '#ffffff'),
    'globalhits': ('HITS', '#3498db', '#ffffff')
}

def is_white_or_checkerboard(r, g, b):
    if r > 180 and g > 180 and b > 180:
        if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
            return True
    return False

def remove_background(img_path):
    img = Image.open(img_path).convert('RGBA')
    width, height = img.size
    pixels = img.load()
    
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
                        
    for x in range(width):
        for y in range(height):
            if not visited[x][y]:
                r, g, b, a = pixels[x, y]
                if is_white_or_checkerboard(r, g, b):
                    pixels[x, y] = (0, 0, 0, 0)
                    
    img.save(img_path, 'WEBP', quality=95)

def generate_avatar(name, text, bg_color, fg_color):
    img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([30, 30, 270, 270], fill=bg_color, outline='#ffffff', width=6)
    text_w = len(text) * 16
    draw.text((150 - text_w, 130), text, fill=fg_color, font=None, size=32)
    dest_path = os.path.join(dest_dir, f"{name}.webp")
    img.save(dest_path, 'WEBP', quality=95)
    print(f"Generated avatar for {name}")

def get_wikimedia_url(title):
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
    headers = {'User-Agent': 'MyPersonalPortfolioDownloader/1.1 (mycontact@portfolio.com)'}
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            pages = res_data.get('query', {}).get('pages', {})
            for page in pages.values():
                info = page.get('imageinfo', [])
                if info:
                    raw_url = info[0].get('url')
                    # Convert raw SVG url to 500px PNG thumb url
                    # Format: https://upload.wikimedia.org/wikipedia/commons/x/xx/Name.svg
                    # Target: https://upload.wikimedia.org/wikipedia/commons/thumb/x/xx/Name.svg/500px-Name.svg.png
                    if raw_url.endswith('.svg'):
                        parts = raw_url.split('/commons/')
                        if len(parts) == 2:
                            subpath = parts[1]
                            filename = subpath.split('/')[-1]
                            return f"https://upload.wikimedia.org/wikipedia/commons/thumb/{subpath}/500px-{filename}.png"
                    return raw_url
    except Exception as e:
        print(f"Error querying API for {title}: {e}")
    return None

# Process main brands
headers = {'User-Agent': 'MyPersonalPortfolioDownloader/1.1 (mycontact@portfolio.com)'}

for name, title in queries.items():
    dest_path = os.path.join(dest_dir, f"{name}.webp")
    
    # Check if we should download NTT Data logo as fallback for everis
    if name == 'everis':
        title = 'File:NTT DATA logo.svg'
        
    print(f"Querying Wikimedia API for {name} ({title})...")
    time.sleep(2) # rate limit prevention
    img_url = get_wikimedia_url(title)
    
    if img_url:
        try:
            print(f"Downloading {name} from {img_url}...")
            time.sleep(2)
            req = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as response, open(dest_path, 'wb') as out_file:
                out_file.write(response.read())
            remove_background(dest_path)
            print(f"Successfully downloaded and processed {name} logo!")
        except Exception as e:
            print(f"Download failed for {name}: {e}. Generating fallback avatar...")
            fallback_text = name.upper()[:5]
            color_map = {
                'liverpool': ('LVP', '#d63031', '#ffffff'),
                'oxxo': ('OXXO', '#e74c3c', '#f1c40f'),
                'santander': ('SAN', '#e74c3c', '#ffffff'),
                'citibanamex': ('BNMX', '#0984e3', '#ffffff'),
                'pepsico': ('PEP', '#0984e3', '#ffffff'),
                'telcel': ('TCL', '#0984e3', '#ffffff'),
                'italika': ('ITK', '#27ae60', '#f1c40f'),
                'everis': ('NTT', '#004481', '#ffffff')
            }
            text, bg, fg = color_map.get(name, (fallback_text, '#2c3e50', '#ffffff'))
            generate_avatar(name, text, bg, fg)
    else:
        print(f"No Wikimedia URL found for {name}. Generating fallback...")
        fallback_text = name.upper()[:5]
        color_map = {
            'liverpool': ('LVP', '#d63031', '#ffffff'),
            'oxxo': ('OXXO', '#e74c3c', '#f1c40f'),
            'santander': ('SAN', '#e74c3c', '#ffffff'),
            'citibanamex': ('BNMX', '#0984e3', '#ffffff'),
            'pepsico': ('PEP', '#0984e3', '#ffffff'),
            'telcel': ('TCL', '#0984e3', '#ffffff'),
            'italika': ('ITK', '#27ae60', '#f1c40f'),
            'everis': ('NTT', '#004481', '#ffffff')
        }
        text, bg, fg = color_map.get(name, (fallback_text, '#2c3e50', '#ffffff'))
        generate_avatar(name, text, bg, fg)

# Generate other consulting avatars
for name, data in fallbacks.items():
    text, bg, fg = data
    generate_avatar(name, text, bg, fg)

print("\nLogo processing finished successfully!")
