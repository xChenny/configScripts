# This is a script to randomly choose a wallpaper

from os import listdir
from os.path import isfile, join
from random import random
from pywal import image, wallpaper

pictures_path = "/home/achen/Pictures"

def pick_img(pictures_dir):
    # list and randomly choose img_cat
    image_categories = listdir(pictures_dir)
    category = image_categories[int(random() * len(image_categories))]
    pictures_dir += "/"
    pictures_dir += category
    # return a random image path inside of the random category
    return image.get(pictures_dir)

wallpaper.change(pick_img(pictures_path))
