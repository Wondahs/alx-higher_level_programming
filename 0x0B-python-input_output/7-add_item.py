#!/usr/bin/python3
#load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
#save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys

arguments = []
for item in sys.argv[1:]:
    arguments.append(str(item))
print(arguments)
