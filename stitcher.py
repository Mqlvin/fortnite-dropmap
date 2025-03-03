import math
import pathlib

from PIL import Image

# we get all files in dl-out to check they exist when doing the loading loop, get a sample image and get dimension of grid
files = [str(path) for path in pathlib.Path("./dl-out").glob("*.jpg")]

def stitch(path_list: list[str]):
    # holds the unit dimension(s) of the (square) grid
    grid_dimension = int(math.sqrt(len(path_list)))

    # sample surface, dimension of sample surface (square dimensions), dimension of final surface (also has square dimensions)
    sample = Image.open(path_list[0])
    img_dimension = sample.size[0]
    output_dimension = img_dimension * grid_dimension

    # intialise final surface
    stitched_image = Image.new("RGB", (output_dimension, output_dimension)) 

    # unit coordinates for grid
    for grid_x in range(0, grid_dimension):
        for grid_y in range(0, grid_dimension):

            # dimensions on final surface
            x = grid_x * img_dimension
            y = grid_y * img_dimension

            subimg_path = f"./dl-out/{grid_x}-{grid_y}.jpg"
            if not pathlib.Path(subimg_path).exists():
                print(f"Error: Not all sub-images exist (x:{grid_x} y:{grid_y}). Skipping subimage...")
                continue
            
            # images exists so load it and stitch it
            stitched_image.paste(Image.open(f"./dl-out/{grid_x}-{grid_y}.jpg"), (x, y))

    return stitched_image


output_image = stitch(files)
output_image.save("map.jpg", "JPEG")

print("Good job!\nThere should be a file called map.jpg in this directory.\nNow, edit `plotter.py`'s target_x and target_y values to where you want to drop.\nThen, run `python plotter.py`")
