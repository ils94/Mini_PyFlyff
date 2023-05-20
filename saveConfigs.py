import json
import os


def save_config(entry1, entry2, entry3):
    data = {
        "value1": entry1,
        "value2": entry2,
        "value3": entry3
    }

    with open("config.json", "w") as json_file:
        json.dump(data, json_file)


def open_config():
    file_path = "config.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

            value1 = data['value1']
            value2 = data['value2']
            value3 = data['value3']

            return value1, value2, value3
    else:
        print("no file")
