import math
import random

import requests
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

tuple_input = input("Enter the script output: ").split("-")
target_tuples = [tuple(x.split(",")) for x in tuple_input]


def get_url(target_x, target_y, bs_x, bs_y, be_x, be_y):
    return f"https://www.landingtutorial.com/ajax/preanalyze.php?targetX={target_x}&targetY={target_y}&busStartX={bs_x}&busStartY={bs_y}&busStopX={be_x}&busStopY={be_y}"

# returns tuple of coord tuples (drop, deploy, height)
def get_data(target_x, target_y, bs_x, bs_y, be_x, be_y):
    response = (requests.get(get_url(target_x, target_y, bs_x, bs_y, be_x, be_y)).content).decode("utf-8")
    data = response[5:len(response)-6].split(",") # get rid of <res> tags
    return ((float(data[0]) * 500.0, float(data[1]) * 500.0), (float(data[2]) * 500.0, float(data[3]) * 500.0), (float(data[4]),))


# point tup, scale int, offset tup
def tup_point_transform(point, scale, offset):
    return (int(point[0] * scale + offset[0] * scale), int(point[1] * scale + offset[1] * scale))

def center_image_coordinates(img_size, point):
    return (int(point[0] + img_size / 2), int(point[1] + img_size / 2))



image = Image.open("./map.jpg")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('./assets/font.ttf', 24)
map_scale = int(image.size[0] / 500)
offset_fix = 5 * map_scale




# configurable
bound = 10 * map_scale
target_x = 216
target_y = 283
# end of configurable




x_min = image.size[0]
x_max = 0
y_min = x_min
y_max = 0

transformed_target = tup_point_transform((target_x, target_y), map_scale, (2, 4))

for idx, i in enumerate(target_tuples):
    print(f"Determining point {idx + 1}/{len(target_tuples)}")
    point = (get_data(target_x, target_y, i[0], i[1], i[2], i[3]))

    transformed_point = tup_point_transform(point[1], map_scale, (5.4, 6))

    if abs(transformed_target[0] - transformed_point[0]) > map_scale * 70 or abs(transformed_target[1] - transformed_point[1]) > map_scale * 70:
        continue

    if point[2][0] != 100.0:
        draw.text((transformed_point[0] + 10, center_image_coordinates(72, transformed_point)[1] + 18), f"{round(point[2][0])}m", (255, 0, 0), font=font)

    x_min = min(x_min, transformed_point[0])
    x_max = max(x_max, transformed_point[0])
    y_min = min(y_min, transformed_point[1])
    y_max = max(y_max, transformed_point[1])

    image.paste(Image.open("./assets/marker.jpg"), center_image_coordinates(72, transformed_point))

image.paste(ImageEnhance.Brightness(Image.open("./assets/marker.jpg")).enhance(0.0), center_image_coordinates(72, tup_point_transform((target_x, target_y), map_scale, (2, 4))))

x_min -= bound
x_max += bound
y_min -= bound
y_max += bound

image = image.crop((x_min, y_min, x_max, y_max))

image.save("./marked.jpg", "JPEG")
print("Image saved to ./marked.jpg")

