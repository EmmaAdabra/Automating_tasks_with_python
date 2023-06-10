# Process Text Files with Python Dictionaries and Upload to Running Web Service

This project focuses on automating the processing of text files containing customer reviews and uploading them to a running web service.
To accomplish this, the `run.py` script is use to converts the feedback from .txt files into Python dictionaries and then uploads the data to your company's website, which is currently built using Django.

## Getting Started

To begin, make sure you have Python installed on your machine. Additionally, ensure that the necessary dependencies, such as the requests module, are installed

## Functions

### `get_users_feedback(file_dir_path)`

This function takes the path to the user's feedback directory as a parameter and returns a list of all feedbacks in the directory.

- **Parameters**
  - `file_dir_path` (str): The path to the user's feedback directory.

- **Returns**
  - `feedback_file_list` (list): A list of all feedbacks in the directory, with each item being the full path to a feedback file.

## `parse_feedback_file(feedback_file_list)`

This function takes a list of user feedback file paths as input. It opens each text file, parses the feedback text into a dictionary, and returns a list of users' feedback dictionaries.

- **Parameters**
  - `feedback_file_list` (list): A list of file paths to the user feedback files.

- **Returns**
  - `feedback_dict` (list): A list of dictionaries, where each dictionary represents the parsed feedback data from a file. The dictionary has the following keys:
  - `title` (str): The title of the feedback.
  - `name` (str): The name of the user.
  - `date` (str): The date of the feedback.
  - `feedback` (str): The content of the feedback.
  
## `post_to_web(feedback_dict)`

This function takes a dictionary of users' feedback and posts it to a web server using a query string.

- **Parameters**
  - `feedback_dict` (dict): A dictionary containing the users' feedback data. Each dictionary represents the feedback from a user, with keys corresponding to the data fields.
- **Returns**
  - A dictionary with the following keys:
  - `success` (int): The number of successful posts.
  - `failed` (int): The number of failed posts.

## main()

This function controls the program flow and logic.

### Steps

1. Checks if the source directory exists.
2. Checks if the source directory is empty.
3. Calls the `get_users_feedback` function with the `feedback_files_dir` parameter to get a list of user feedback files.
4. Calls the `parse_feedback_file` function with the `feedback_list` parameter to parse the feedback files and obtain a list of dictionaries representing the feedback data.
5. Calls the `post_to_web` function with the `feedback_dict` parameter to post the feedback data to a web server.
6. Prints the number of successfully posted feedbacks and the number of failed posts.
