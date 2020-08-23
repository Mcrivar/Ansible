#!/usr/bin/python

import os

current_folder = os.path.dirname(os.path.realpath(__file__))
region = os.path.basename(os.path.normpath(current_folder))
json_inventory = current_folder + '/hosts.json'

with open(json_inventory) as f:
    print(f.read())
