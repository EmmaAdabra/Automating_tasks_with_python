#!/usr/bin/env python3

from PIL import Image
import os

home = os.path.expanduser("~")
dir_path = os.path.join(home, "images")
save_path = os.path.join(home, "icons")


def get_images(dir_path):
    """create a list of address path to the images"""
    images = [
        os.path.join(dir_path, img_name)
        for img_name in os.listdir(dir_path)
        if img_name[0] != "."
    ]
    return images


def process_img(img):
    """convert image to RGB mode, resize image to 128x128 and rotate it -90 degree clockwise"""
    img = img.convert("RGB")
    img = img.resize((128, 128))
    return img.rotate(-90)


def save_as_jpeg(img_name, img):
    """save image to a new directory in JPEG format"""
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    output_path = os.path.join(save_path, img_name + ".jpeg")
    img.save(output_path)


def main():
    if not os.path.exists(dir_path):
        print("Directory does not exist")
    if len(os.listdir(dir_path)) == 0:
        print("Directory is empty")

    for image in get_images(dir_path):
        img_name = os.path.basename(image)
        img = Image.open(image)
        img = process_img(img)
        save_as_jpeg(img_name, img)


if __name__ == "__main__":
    main()
