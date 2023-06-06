#!/usr/bin/env python3

from PIL import Image
import unittest
import os

home = os.path.expanduser("~")
dir_path = os.path.join(home, "images")
save_path = "ls /opt/icons"

def get_img_path(dir_path):
    """create a list of address path to the images"""
    image_paths = [os.path.join(dir_path, img_name) for img_name in os.listdir(dir_path)]
    return image_paths
   

def process_img(img):
    """convert image to RGB mode and rotate it 90 degree clockwise"""
    img = img.convert("RGB")
    return img.rotate(90)


def main():
    # count = 0
    # if not os.path.exists(dir_path):
        # print("Directory does not exist")
    # if len(os.listdir(dir_path)) == 0:
        # print("Directory is empty")
    # 
    # for img in get_img_path(dir_path):
        # img = Image.open(img)
        # img = process_img(img)
        # print(img.mode)
        # if count == 5:
            # break
        # count += 1
    pass
if __name__ == "__main__":
    main()
