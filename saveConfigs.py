import json
import os
import globalVariables
import keyboardListener
from tkinter import messagebox


def create_json_config(data_tuple):
    data = {

        "value1": data_tuple[0],
        "value2": data_tuple[1],
        "value3": data_tuple[2],
        "value4": data_tuple[3],
        "value5": data_tuple[4],
        "value6": data_tuple[6],
        "value7": data_tuple[7],
        "value8": data_tuple[8],
        "value9": data_tuple[9],
        "value10": data_tuple[10],
        "value11": data_tuple[12],
        "value12": data_tuple[13]

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
                value6 = data['value6']
                value7 = data['value7']
                value8 = data['value8']
                value9 = data['value9']
                value10 = data['value10']
                value11 = data['value11']
                value12 = data['value12']

                return value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12
        else:

            return "", "", "", "", 0, "", "", "", "", "", "", ""

    except Exception as e:

        messagebox.showerror("Error", f"Something went wrong when loading your config.json!\n\n{str(e)}")

        return "", "", "", "", 0, "", "", "", "", "", "", ""


def save_key_configs(data_tuple):
    globalVariables.alt_controller_hotkey_list = data_tuple[0].split(",")

    globalVariables.macro_loop_hotkeys = data_tuple[1].split(",")

    globalVariables.macro_loop_hotkey_delay = data_tuple[2].split(",")

    keyboardListener.set_macro_loop_shortcut(data_tuple[3], data_tuple[5])

    globalVariables.buffer_hotkeys = data_tuple[6].split(",")

    globalVariables.buffs_hotbar = data_tuple[7]

    globalVariables.previous_hotbar = data_tuple[8]

    globalVariables.buffer_delay = data_tuple[9]

    keyboardListener.set_buffer_shortcut(data_tuple[10], data_tuple[11])

    globalVariables.gt_buffer_hotkey = data_tuple[12]

    globalVariables.gt_buffer_delay = data_tuple[13]

    create_json_config(data_tuple)
