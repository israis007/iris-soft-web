from PIL import Image
img = Image.open('C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782106922696.png')
print("Top-left pixel (0,0):", img.getpixel((0, 0)))
print("Pixel (20,0):", img.getpixel((20, 0)))
print("Pixel (40,0):", img.getpixel((40, 0)))
