import os
from PIL import Image, ImageDraw

dest_dir = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos'
os.makedirs(dest_dir, exist_ok=True)

# 1. Legalario Logo (Stylized document/signature icon in teal)
img_l = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
draw_l = ImageDraw.Draw(img_l)
# Draw document shape
draw_l.rounded_rectangle([70, 50, 230, 250], radius=15, fill=None, outline='#00b894', width=8)
# Draw lines representing text
draw_l.line([100, 100, 200, 100], fill='#00b894', width=8)
# Draw a check mark or quill representation
draw_l.line([100, 150, 170, 150], fill='#00b894', width=8)
draw_l.line([100, 200, 150, 200], fill='#00b894', width=8)
# Draw signature loop
draw_l.ellipse([180, 180, 230, 220], outline='#ff7675', width=6)
img_l.save(os.path.join(dest_dir, 'legalario.webp'), 'WEBP', quality=85)

# 2. Softtek Logo (Stylized geometric 'S' in blue & orange)
img_s = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
draw_s = ImageDraw.Draw(img_s)
# Draw stylized arcs/lines representing a modern S
draw_s.arc([60, 60, 240, 240], start=180, end=360, fill='#0984e3', width=16)
draw_s.arc([60, 60, 240, 240], start=0, end=180, fill='#ff7675', width=16)
draw_s.line([60, 150, 240, 150], fill='#0984e3', width=16)
img_s.save(os.path.join(dest_dir, 'softtek.webp'), 'WEBP', quality=85)

# 3. Qualtop Logo (Stylized tech 'Q' in green/blue)
img_q = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
draw_q = ImageDraw.Draw(img_q)
# Draw circle for Q
draw_q.ellipse([60, 60, 220, 220], outline='#00cec9', width=16)
# Draw tail of Q
draw_q.line([180, 180, 240, 240], fill='#0984e3', width=16)
img_q.save(os.path.join(dest_dir, 'qualtop.webp'), 'WEBP', quality=85)

print("Generated logos successfully!")
