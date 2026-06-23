from PIL import Image

src = 'C:/Users/mc_dj/.gemini/antigravity-ide/brain/dd7e2343-a56d-408e-b3d4-ced244d80e64/media__1782108240465.png'
dest = 'c:/Users/mc_dj/AndroidStudioProjects/iris-soft-web/resources/logos/legalario.webp'

img = Image.open(src)
img.save(dest, 'WEBP', quality=95)
print("Successfully converted Legalario logo to WebP format!")
