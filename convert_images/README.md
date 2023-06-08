# Scale and convert images using PIL

This tasks makes uses the Python Imaging Library and four functions to do the following to a batch of images:  

- Open an image
- covert mode
- Rotate an image
- Resize an image
- Save an image in a specific format in a separate directory  

The Python Imaging Library (PIL) is a powerful library for working with images in Python. It provides a wide  
range of image processing capabilities, allowing you to load, manipulate, and save various image file formats.

## Functions

### `get_images(dir_path)`
>
>This function takes a directory path as input and creates a list of images to be converted.  
>It scans the directory for image files and filters out any files starting with a dot (hidden files) to avoid  
>`UnidentifiedImageError` error  
>**Parameters**: `dir_path` (str): The path to the directory containing the images.  
>**Returns**: `images` (list): A list of image file paths  

### `process_img(img)`
>
>This function takes an image object as input and performs the following operations on it:
>
> - Converts the image to RGB mode.  
> - Resizes the image to 128x128 pi
> - Rotates the image -90 degrees clockwise.
>**Parameters**:
  -`img` (PIL Image object): The input image to be processed.
>**Returns**:
  -`img` (PIL Image object): The processed image.

### `save_as_jpeg(img_name, img)`
>
>This function takes an image name and image object as input and performs the following operations:
>
> - Checks if the destination directory exists and creates it if not.
> - Saves the image in JPEG format to the destination directory.
> - Increments a global variable that keeps count of successfully converted image `count` by 1.  
>**Parameters**
> - `img_name` (str): The name of the image file.
> - `img` (PIL Image object): The image to be saved.  

### `main()`
>
>
>This function controls the program flow and logic. It performs the following operations:
>
>- Checks if the source directory exists and prints an appropriate message if it doesn't.
>- Checks if the source directory is empty and prints an appropriate message if it is.
>- Attempts to convert each image in the source directory using the `get_images`, `process_img`, and `save_as_jpeg` functions.
>- If any exception occurs during the conversion process, it prints an error message and exits the program.
>- Finally, it prints a summary of the number of images successfully converted, along with their mode, size, and format.

### [images/]()

The image directory contains 100 images images that will be process and converted to JPEG format.
**Image properties**:

- Mode: LA
- Size: 192 x 192
- Format: TIFF
- Rotated 90° anti-clockwise  
  
>N/B: All images must be converted to RGB mode before it can be successfully save in JPEG format.
