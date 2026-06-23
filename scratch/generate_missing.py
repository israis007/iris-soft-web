import os
from PIL import Image, ImageDraw

dest_dir = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos'

missing = {
    'agilethought': ('AGILE', '#1abc9c', '#ffffff'),
    'ids': ('IDS', '#34495e', '#ffffff'),
    'globalhits': ('HITS', '#3498db', '#ffffff')
}

def generate_avatar(name, text, bg_color, fg_color):
    img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([30, 30, 270, 270], fill=bg_color, outline='#ffffff', width=6)
    text_w = len(text) * 16
    draw.text((150 - text_w, 130), text, fill=fg_color, font=None, size=32)
    dest_path = os.path.join(dest_dir, f"{name}.webp")
    img.save(dest_path, 'WEBP', quality=95)
    print(f"Generated avatar for {name}")

for name, data in missing.items():
    text, bg, fg = data
    generate_avatar(name, text, bg, fg)
