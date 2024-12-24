# Fortnite Dropmap Generator
A free-to-use Fortnite drop map generator, using the [landingtutorial.com](https://landingtutorial.com) API to generate drops, and the [fortnite.gg](https://fortnite.gg) website to download the visuals.

## Prerequisites
You will need Python's `pillow` library. Install this appropriately, for example `pip3 install pillow` or `pacman -Sy python-pillow`

## How to use
*If you have any difficulties with these instructions, you can create an issue on the repo, or contact me on Discord (@mqlvin) or Matrix (mqlvin@nope.chat)*<br>
### Generating the map image
First, you need to generate a map image for the program to use. It will make many requests to fortnite.gg for their pre-existing map.<br>
There are optional configurables in the `downloader.py` file, such as map zoom (I would recommend 5) and map ID, which ideally is set to the current season.<br>
<br>
Once configured, run `python downloader.py`.<br>
It will create a folder called `./dl-out` with a lot of images.<br>
<br>
Next, you will want to stitch the images together into a single big image.<br>
To do this, run `python stitcher.py`.<br>
It will create an image called `map.jpg`.<br>
<br><br>
### Generating the drops
Open the `devtools.js` file in this repository - you will find some Javascript code.<br>
Follow the instructions within the top of the file. It also has configurable options although the default are quite good.<br>
This should result in you having a long string of numbers, such as `1,1,499,499-1,283,499,4...`. Copy this to your clipboard.<br>
<br>
Next configure `plotter.py`. You can change the `target_x` and `target_y` variables to change the target drop position.
Run `python plotter.py` and you should be prompted to enter the script output. Paste the set of numbers on your clipboard, and press enter.<br>
<br>
Now the script will contact the landingtutorial.com API for the appropriate drops. This could take a few minutes depending on the number of drops generated.<br>
And that's it :)

## Result
The resulting dropmap will be in a file called `./marked.jpg`.<br>
It has a few features:
- Red boxes are where you should start gliding.
- If a red box has a number below it, you should start gliding at that altitude. Otherwise, start gliding at 100m (the auto-glide point).
- The black box which is probably somewhere near the middle is your drop target.

Here is an example of a generated dropmap below:
![Example dropmap image](https://i.imgur.com/XudJNtP.jpeg)


## Licensing and Credits
Thanks to fortnite.gg's and landingtutorial.com's free API's.<br>
All code in this repository is written by me and licensed under the [CC By-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en). Importantly, I strictly prohibit usage of my code for commercial purposes.<br>
<br>
If you have any issues or questions you can contact me on Discord (@mqlvin) or Matrix (mqlvin@nope.chat). <br>
Enjoy. ❤️

