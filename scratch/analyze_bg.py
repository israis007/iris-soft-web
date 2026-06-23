import os
from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782106922696.png'
img = Image.open(src).convert('RGBA')
width, height = img.size
pixels = img.load()

# Create a mask of what remove_bg.py currently does (outer flood fill)
visited = [[False for _ in range(height)] for _ in range(width)]

def is_bg_color(r, g, b):
    if r > 175 and g > 175 and b > 175:
        if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
            return True
    return False

queue = []
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

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while queue:
    x, y = queue.pop(0)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if not visited[nx][ny]:
                r, g, b, a = pixels[nx, ny]
                if is_bg_color(r, g, b):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# Now, let's find all pixels that were NOT visited by the flood fill,
# but which match is_bg_color. These are either inside the loops or inside the snake.
potential_bg_holes = []
for x in range(width):
    for y in range(height):
        if not visited[x][y]:
            r, g, b, a = pixels[x, y]
            if is_bg_color(r, g, b):
                potential_bg_holes.append((x, y))

print(f"Total potential bg hole pixels: {len(potential_bg_holes)}")

# Let's group them into connected components to see their sizes!
visited_holes = [[False for _ in range(height)] for _ in range(width)]
components = []

for hx, hy in potential_bg_holes:
    if visited_holes[hx][hy]:
        continue
    # BFS to find component
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
    components.append(comp)

components.sort(key=len, reverse=True)
print(f"Found {len(components)} separate components matching bg color inside the non-visited areas:")
for i, comp in enumerate(components[:10]):
    print(f"  Component {i}: size {len(comp)} pixels, bounding box: x in [{min(x for x, y in comp)}, {max(x for x, y in comp)}], y in [{min(y for x, y in comp)}, {max(y for x, y in comp)}]")
