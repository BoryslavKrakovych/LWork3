import math
from PIL import Image, ImageDraw
img = Image.new('RGBA', (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)
with open("DS0.txt", "r") as file:
    for line in file:
        coords=line.split()
        i = int(coords[1]) - 480
        j = int(coords[0]) - 480
        x = math.cos(math.radians(40)) * i - math.sin(math.radians(40)) * j
        y = math.sin(math.radians(40)) * i + math.cos(math.radians(40)) * j
        draw.line((x + 480, y + 480, x + 481, y + 481), fill=(0, 190, 255))
img.show()
img.save('LAB3.png')
