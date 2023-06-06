#!/usr/bin/env python3

from PIL import Image
import unittest
import os

home = os.path.expanduser("~")
file_path = os.path.join(home, "images")
save_path = "ls /opt/icons"


def rotate_img():
    pass


def get_img_path(file_path):
    """create a list of address path to the images"""
    image_paths = [
        os.path.join(file_path, img_name) for img_name in os.listdir(file_path)
    ]
    print(image_paths)
    return image_paths


def main():
    pass


if __name__ == "__main__":
    main()
