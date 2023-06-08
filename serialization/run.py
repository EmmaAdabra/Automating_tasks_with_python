#!/usr/bin/env python

# import the required module
import os
import json
import requests

# create path to users_feedback files
project_path = os.path.join(os.path.expanduser("~"), os.path.join
("automate_real_world_tasks", "serialization"))
feedback_txt_path = os.path.join(project_path, "users_feedback")

print(feedback_txt_path)