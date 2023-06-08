#!/usr/bin/env python

# import the required module
import os
import json
import requests

# create path to users_feedback files
project_path = os.path.join(
    os.path.expanduser("~"), os.path.join("automate_real_world_tasks", "serialization")
)
feedback_file_path = os.path.join(project_path, "users_feedback")


def get_users_feedback(file_path):
    """get path to user's feedback directory as parameter, return a list of all feedbacks in the dir"""
    users_feedback = [
        os.path.join(file_path, txt_file) for txt_file in os.listdir(file_path)
    ]  # create a list of users feedback
    return users_feedback