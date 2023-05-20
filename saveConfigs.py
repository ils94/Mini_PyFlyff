import json
import os
import globalVariables
import keyboardListener


def create_json_config(entry1, entry2, entry3, entry4, checkbox_value):
    data = {
        "value1": entry1,
        "value2": entry2,
        "value3": entry3,
        "value4": entry4,
        "value5": checkbox_value
    }

    with open("config.json", "w") as json_file:
        json.dump(data, json_file)


def open_json_config():
    try:
        file_path = "config.json"

        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                data = json.load(json_file)

                value1 = data['value1']
                value2 = data['value2']
                value3 = data['value3']
                value4 = data['value4']
                value5 = data['value5']

                return value1, value2, value3, value4, value5
        else:
            return "", "", "", "", 0
    except Exception as e:
        print(e)
        os.remove("config.json")
        return "", "", "", "", 0


def save_key_configs(entry1, entry2, entry3, entry4, checkbox, function):
    globalVariables.alt_control_key_list = entry1.get().split(",")

    globalVariables.mini_ftool_keys = entry2.get().split(",")
    globalVariables.mini_ftool_key_timers = entry3.get().split(",")

    keyboardListener.set_mini_ftool_shortcut(entry4.get(), function)

    create_json_config(entry1.get(), entry2.get(), entry3.get(), entry4.get(), checkbox)
