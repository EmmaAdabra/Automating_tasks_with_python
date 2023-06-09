#!/usr/bin/env python

# import the required module
import os
import json
import requests

# create path to the project directory
project_path = os.path.join(
    os.path.expanduser("~"), os.path.join("automate_real_world_tasks", "serialization")
)
# create path to the directory containing  user's feedback
feedback_files_dir = os.path.join(project_path, "users_feedback")


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

    # iterate through feedback file in the list
    for feedback in feedback_file_list:
        add_feedback = (
            {}
        )  # tmp dictionary use to add user's feedback dictionary to the list

        # open each feedback file in txt format
        with open(feedback, mode="r", newline="") as feedback_txt:
            # add the content of the feedback file to a list
            data = [row.strip() for row in feedback_txt.readlines()]
        # create a key value pair (dictionary) for each content of the feedback file

        (
            add_feedback["title"],
            add_feedback["name"],
            add_feedback["date"],
            add_feedback["feedback"],
        ) = data
        feedback_dict.append(add_feedback)  # append the dictionary to a list
    return feedback_dict


def post_to_web(feedback_dict):
    """get users feedback as dictionary and post it to a web server using query string"""
    response = requests.post("url/api", json=feedback_dict)
    return response.status_code
