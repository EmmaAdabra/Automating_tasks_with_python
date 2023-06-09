#!/usr/bin/env python

# import the required module
import os
import requests

# path user's feedback dir
feedback_files_dir = os.path.join(os.getcwd(), "serialization/users_feedback")


def get_users_feedback(file_dir_path):
    """get path to user's feedback directory as parameter, return a list of all feedbacks in the dir"""
    # list of users feedback
    feedback_file_list = [
        os.path.join(file_dir_path, txt_file) for txt_file in os.listdir(file_dir_path)
    ]  # create a list of users feedback
    return feedback_file_list


def parse_feedback_file(feedback_file_list):
    """get list of user feedbacks file path, open the text file, parse the feedback txt to dictionary and return a list users feedback dictionary"""

    feedback_dict = []  # holds the user's feedback dictionary
    # feedback dictionary keys
    keys = ["title","name","date","feedback",]

    # iterate through feedback file in the list
    for feedback in feedback_file_list:
        # open each feedback file in txt format
        with open(feedback, mode="r", newline="") as feedback_txt:
            # add the content of file to a list
            data = [row for row in feedback_txt.read().splitlines()]
        # create a key value pair for each content of the feedback file
        feedback_dict.append(dict(zip(keys, data)))
    return feedback_dict


def post_to_web(feedback_dict):
    """get users feedback as dictionary and post it to a web server using query string"""
    failed = 0  # number of failed post
    success = 0  # number of successful post

    for feedback_data in feedback_dict:
        response = requests.post("http://<url/api>", json=feedback_data)
        if response.status_code == 201:
            success += 1
        else:
            failed += 1
    return {"success": success, "failed": failed}


def main():
    """controls program flow and logic"""
    # check if source directory exist
    if not os.path.exists(feedback_files_dir):
        print("Directory does not exist")
    # check if source directory is empty
    if len(os.listdir(feedback_files_dir)) == 0:
        print("Directory is empty")

    # passing the required parameter for each function sequentially
    feedback_list = get_users_feedback(feedback_files_dir)
    feedback_dict = parse_feedback_file(feedback_list)
    post_feedback = post_to_web(feedback_dict)
    print(f"Posted: {post_feedback[1]} feedbacks\nFailed post: {post_feedback[1]}")


# only run script as main module
if __name__ == "__main__":
    main()
