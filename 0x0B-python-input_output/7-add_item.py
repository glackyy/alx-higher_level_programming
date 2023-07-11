#!/usr/bin/python3
"""Add all args to a Python list and save them to a file"""
import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []
data.extend(sys.argv[1:])
save_to_json_file(data, filename)
