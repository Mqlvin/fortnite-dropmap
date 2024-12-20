import concurrent.futures
import pathlib
import time
from os import wait

import requests


def download_image(base_url, save_dir, x, y):
    request_url = base_url + f"{x}/{y}.jpg"
    request_content = requests.get(request_url).content

    with open(f"{save_dir}/{x}-{y}.jpg", "wb") as file:
        file.write(request_content)

# to be put in thread pool
def download_column(col_id, rows, rest_ms):
    for grid_y in range(0, rows):
        download_image(base_url, save_dir, col_id, grid_y)
        time.sleep(rest_ms / 1000)




## CONFIGURATION ##
save_dir = "./dl-out"
pathlib.Path(save_dir).mkdir(exist_ok=True)

zoom_level = 5
map_id = "33.01"

base_url = f"https://fortnite.gg/maps/{map_id}/{zoom_level}/"

delay_ms = 500
###################



# images are on xy grid from coords 0 -> 127
grid_unit_size = int(128 / (2 ** (7 - zoom_level)))
print(f"Downloading {grid_unit_size ** 2} images")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(download_column, i, grid_unit_size, delay_ms) for i in range(0, grid_unit_size)]
    print(f"Spawned {len(futures)} workers...")

    executor.shutdown(wait=True)

