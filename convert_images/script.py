#!/usr/bin/env python3

from PIL import Image
import os
import sys

count = 0  # use to keep track of successfully converted images
home = os.path.join(
    os.path.expanduser("~"), "automate_real_world_tasks"
)  # get full path to user dir
dir_path = os.path.join(
    home, os.path.join("convert_images", "images")
)  # create full path to images source dir
save_path = os.path.join(
    home, os.path.join("convert_images", "icons")
)  # create full path to dest (save) dir


def get_images(dir_path):
    """create a list of images to be converted"""
    images = [
        os.path.join(dir_path, img_name)
        for img_name in os.listdir(dir_path)
        if img_name[0] != "."
    ]
    return images


def process_img(img):
    """convert image to RGB mode, resize image to 128x128 and rotate it -90 degree clockwise"""
    img = img.convert("RGB")  # change image mode to RGB
    img = img.resize((128, 128))  # resize image to 128 x 128
    return img.rotate(-90)  # rotate return image to 90 deg clockwise direction


def save_as_jpeg(img_name, img):
    """save image to a new directory in JPEG format"""
    # check if destination dir exists and create one if not
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    img.save(os.path.join(save_path, img_name + ".jpeg"))  # save image in format
    global count
    count += 1  # Increments the global variable count


def main():
    """controls program flow and logic"""
    # check if source directory exist
    if not os.path.exists(dir_path):
        print("Directory does not exist")
    # check if source directory is empty
    if len(os.listdir(dir_path)) == 0:
        print("Directory is empty")

    try:
        # pass each image obj to the appropriate function
        for image in get_images(dir_path):
            img_name = os.path.basename(image)
            img = Image.open(image)
            img = process_img(img)
            save_as_jpeg(img_name, img)
    except Exception as e:
        print(f" Error!!! Conversion Aborted\n{e}")
        sys.exit(1)

    print(
        f"{count} Images successfully converted\nMode: RGB\nSize: 128 x 128\nFormat JPEG\nSaved to ... {save_path}"
    )


# only run script as main module
if __name__ == "__main__":
    main()
