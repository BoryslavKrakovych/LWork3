import math
from PIL import Image, ImageDraw
img = Image.new('L', (960, 540), 255)
draw = ImageDraw.Draw(img)
with open("DS0.txt", "r") as file:
    for line in file:
        coords=line.split()
        i = int(coords[0]) - 480
        j = int(coords[1]) - 480
        x = math.cos(math.radians(40)) * i - math.sin(math.radians(40)) * j
        y = math.sin(math.radians(40)) * i + math.cos(math.radians(40)) * j
        draw.line((x + 480, y + 480, x + 481, y + 481))
img.show()
img.save('LAB3.png')
