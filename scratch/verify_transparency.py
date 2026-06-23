from PIL import Image

path = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/quetzalcoatl.webp'
img = Image.open(path)
print("Format:", img.format)
print("Mode:", img.mode)
print("Size:", img.size)

# Count transparent and semi-transparent pixels
pixels = img.convert('RGBA').getdata()
transparent_count = 0
semi_transparent_count = 0
opaque_count = 0

for p in pixels:
    alpha = p[3]
    if alpha == 0:
        transparent_count += 1
    elif alpha < 255:
        semi_transparent_count += 1
    else:
        opaque_count += 1

print(f"Transparent pixels (alpha == 0): {transparent_count}")
print(f"Semi-transparent pixels (0 < alpha < 255): {semi_transparent_count}")
print(f"Opaque pixels (alpha == 255): {opaque_count}")
print(f"Total pixels: {len(pixels)}")
