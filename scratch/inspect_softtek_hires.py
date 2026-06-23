from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782112712112.png'
img = Image.open(src)
print("Mode:", img.mode)
print("Size:", img.size)

# Inspect some corner/top pixels
print("Top-left pixel (0,0):", img.getpixel((0, 0)))
print("Pixel (20,0):", img.getpixel((20, 0)))
print("Pixel (40,0):", img.getpixel((40, 0)))
