import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782106922696.png'
dest = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/quetzalcoatl.webp'

img = Image.open(src).convert('RGBA')
width, height = img.size
pixels = img.load()

# Create a mask for visited pixels in flood fill
visited = [[False for _ in range(height)] for _ in range(width)]

def is_bg_color(r, g, b):
    # Check if the pixel color matches the checkerboard pattern (greyscale and light)
    if r > 175 and g > 175 and b > 175:
        if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
            return True
    return False

# Flood fill queue for outer background
queue = []

# Add all border pixels to the queue
for x in range(width):
    if is_bg_color(*pixels[x, 0][:3]):
        queue.append((x, 0))
        visited[x][0] = True
    if is_bg_color(*pixels[x, height - 1][:3]):
        queue.append((x, height - 1))
        visited[x][height - 1] = True

for y in range(height):
    if is_bg_color(*pixels[0, y][:3]):
        queue.append((0, y))
        visited[0][y] = True
    if is_bg_color(*pixels[width - 1, y][:3]):
        queue.append((width - 1, y))
        visited[width - 1][y] = True

# Directions for flood fill
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

print(f"Starting flood fill with {len(queue)} seed pixels...")

bg_count = 0
while queue:
    x, y = queue.pop(0)
    # Set this background pixel to fully transparent
    pixels[x, y] = (0, 0, 0, 0)
    bg_count += 1
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if not visited[nx][ny]:
                r, g, b, a = pixels[nx, ny]
                if is_bg_color(r, g, b):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

print(f"Cleared {bg_count} outer background pixels.")

# Now, find all background holes (enclosed components inside the snake body)
potential_holes = []
for x in range(width):
    for y in range(height):
        if not visited[x][y]:
            r, g, b, a = pixels[x, y]
            if is_bg_color(r, g, b):
                potential_holes.append((x, y))

visited_holes = [[False for _ in range(height)] for _ in range(width)]
hole_count = 0

for hx, hy in potential_holes:
    if visited_holes[hx][hy]:
        continue
    
    # BFS to find component size and pixels
    comp = []
    q = [(hx, hy)]
    visited_holes[hx][hy] = True
    while q:
        cx, cy = q.pop(0)
        comp.append((cx, cy))
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                if not visited[nx][ny] and not visited_holes[nx][ny]:
                    r, g, b, a = pixels[nx, ny]
                    if is_bg_color(r, g, b):
                        visited_holes[nx][ny] = True
                        q.append((nx, ny))
    
    # If the component is large enough (i.e. background loop, not a detail inside the snake), clear it
    if len(comp) > 100:
        for cx, cy in comp:
            pixels[cx, cy] = (0, 0, 0, 0)
            bg_count += 1
        hole_count += 1

print(f"Cleared {hole_count} inner background holes. Total cleared pixels: {bg_count}")

# Save optimized WEBP
img.save(dest, 'WEBP', quality=85)
print("Background removed and saved successfully!")
