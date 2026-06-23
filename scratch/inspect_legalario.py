from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782108240465.png'
img = Image.open(src)
print("Mode:", img.mode)
print("Size:", img.size)

# Inspect corner pixels to find what color the background is
print("Top-left pixel (0,0):", img.getpixel((0, 0)))
print("Top-right pixel (width-1,0):", img.getpixel((img.width - 1, 0)))
print("Bottom-left pixel (0,height-1):", img.getpixel((0, img.height - 1)))
print("Bottom-right pixel (width-1,height-1):", img.getpixel((img.width - 1, img.height - 1)))
