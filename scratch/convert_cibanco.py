import os
from PIL import Image

src_cibanco = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782115083939.jpg'
dest_cibanco = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/cibanco.webp'

img_cibanco = Image.open(src_cibanco).convert('RGBA')
width, height = img_cibanco.size
pixels = img_cibanco.load()

# Background threshold for white pixels (checking r, g, b > 230)
def is_white(r, g, b):
    return r > 230 and g > 230 and b > 230

# Flood fill outer background
visited = [[False for _ in range(height)] for _ in range(width)]
queue = []

for x in range(width):
    if is_white(*pixels[x, 0][:3]):
        queue.append((x, 0))
        visited[x][0] = True
    if is_white(*pixels[x, height - 1][:3]):
        queue.append((x, height - 1))
        visited[x][height - 1] = True

for y in range(height):
    if is_white(*pixels[0, y][:3]):
        queue.append((0, y))
        visited[0][y] = True
    if is_white(*pixels[width - 1, y][:3]):
        queue.append((width - 1, y))
        visited[width - 1][y] = True

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
outer_cleared = 0

while queue:
    x, y = queue.pop(0)
    pixels[x, y] = (0, 0, 0, 0)
    outer_cleared += 1
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if not visited[nx][ny]:
                r, g, b, a = pixels[nx, ny]
                if is_white(r, g, b):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# Clear any remaining white pixels inside loops of letters
inner_cleared = 0
for x in range(width):
    for y in range(height):
        if not visited[x][y]:
            r, g, b, a = pixels[x, y]
            if is_white(r, g, b):
                pixels[x, y] = (0, 0, 0, 0)
                inner_cleared += 1

print(f"CIBanco: Cleared {outer_cleared} outer and {inner_cleared} inner white pixels.")
img_cibanco.save(dest_cibanco, 'WEBP', quality=95)
print(f"CIBanco logo saved to {dest_cibanco}")
