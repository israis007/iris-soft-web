import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782108628509.jpg'
dest = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/softtek.webp'

img = Image.open(src).convert('RGBA')
width, height = img.size
pixels = img.load()

# Let's inspect corner colors
print("Corners:")
print("  (0,0):", pixels[0, 0])
print("  (width-1,0):", pixels[width-1, 0])
print("  (0,height-1):", pixels[0, height-1])
print("  (width-1,height-1):", pixels[width-1, height-1])

# A function to check if a pixel is white/near-white background
def is_white_bg(r, g, b):
    # Softtek logo has dark blue (very dark) and green (not white).
    # White background in JPG might be slightly off-white (e.g. 250, 252, 255).
    # Let's check if all channels are > 230
    return r > 230 and g > 230 and b > 230

# Let's do a flood fill to find the outer background first
visited = [[False for _ in range(height)] for _ in range(width)]
queue = []

for x in range(width):
    if is_white_bg(*pixels[x, 0][:3]):
        queue.append((x, 0))
        visited[x][0] = True
    if is_white_bg(*pixels[x, height - 1][:3]):
        queue.append((x, height - 1))
        visited[x][height - 1] = True

for y in range(height):
    if is_white_bg(*pixels[0, y][:3]):
        queue.append((0, y))
        visited[0][y] = True
    if is_white_bg(*pixels[width - 1, y][:3]):
        queue.append((width - 1, y))
        visited[width - 1][y] = True

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
bg_count = 0

while queue:
    x, y = queue.pop(0)
    # Set to transparent
    pixels[x, y] = (0, 0, 0, 0)
    bg_count += 1
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if not visited[nx][ny]:
                r, g, b, a = pixels[nx, ny]
                if is_white_bg(r, g, b):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

print(f"Cleared {bg_count} outer background pixels.")

# Now, let's find any interior holes (like in 'o', 'e', 'R' symbol) that are near-white
# and should also be transparent.
# Since the logo itself has no white parts, any white pixel remaining in the image
# is actually a background hole!
# So we can safely clear any remaining near-white pixels.
inner_bg_count = 0
for x in range(width):
    for y in range(height):
        if not visited[x][y]:
            r, g, b, a = pixels[x, y]
            if is_white_bg(r, g, b):
                pixels[x, y] = (0, 0, 0, 0)
                inner_bg_count += 1

print(f"Cleared {inner_bg_count} inner white hole pixels. Total: {bg_count + inner_bg_count}")

# Let's save the result to webp
img.save(dest, 'WEBP', quality=95)
print("Softtek logo background removed and saved to WebP!")
