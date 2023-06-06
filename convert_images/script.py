#!/usr/bin/env python3

from PIL import Image
import unittest
import os

home = os.path.expanduser("~")
dir_path = os.path.join(home, "images")
save_path = os.path.join(home, "icons")


def get_img_path(dir_path):
    """create a list of address path to the images"""
    image_paths = [
        os.path.join(dir_path, img_name) for img_name in os.listdir(dir_path)
    ]
    return image_paths


def process_img(img):
    """convert image to RGB mode, resize image to 128x128 and rotate it -90 degree clockwise"""
    img = img.convert("RGB")
    img = img.resize(128, 128)
    return img.rotate(-90)


def save_as_jpeg(img_name, img):
    """save image to a new directory in JPEG format"""
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    output_path = os.path.join(save_path, img_name + ".jpeg")
    img.save(output_path)


def main():
    # if not os.path.exists(dir_path):
        # print("Directory does not exist")
    # if len(os.listdir(dir_path)) == 0:
        # print("Directory is empty")

    # for img_path in get_img_path(dir_path):
        # img_name = os.path.basename(img_path)
        # img = Image.open(img_path)
        # img = process_img(img)
        # save_as_jpeg(img_name, img)
    pass


if __name__ == "__main__":
    main()
