import json
import os
import globalVariables
import keyboardListener


def create_json_config(entry1, entry2, entry3, entry4, checkbox_value, entry5, entry6, entry7, entry8, entry9, entry10,
                       entry11):
    data = {
        "value1": entry1,
        "value2": entry2,
        "value3": entry3,
        "value4": entry4,
        "value5": checkbox_value,
        "value6": entry5,
        "value7": entry6,
        "value8": entry7,
        "value9": entry8,
        "value10": entry9,
        "value11": entry10,
        "value12": entry11
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
        print(e)
        os.remove("config.json")
        return "", "", "", "", 0, "", "", "", "", "", "", ""


def save_key_configs(entry1, entry2, entry3, entry4, checkbox, function, entry5, entry6, entry7, entry8, entry9,
                     function2, entry10, entry11):
    globalVariables.alt_controller_hotkey_list = entry1.get().split(",")

    globalVariables.macro_loop_hotkeys = entry2.get().split(",")
    globalVariables.macro_loop_hotkey_delay = entry3.get().split(",")

    keyboardListener.set_macro_loop_shortcut(entry4.get(), function)

    globalVariables.buffer_hotkeys = entry5.get().split(",")

    globalVariables.buffs_hotbar = entry6.get()

    globalVariables.previous_hotbar = entry7.get()

    globalVariables.buffer_delay = entry8.get()

    keyboardListener.set_buffer_shortcut(entry9.get(), function2)

    globalVariables.gt_buffer_hotkey = entry10.get()

    globalVariables.gt_buffer_delay = entry11.get()

    create_json_config(entry1.get(), entry2.get(), entry3.get(), entry4.get(), checkbox, entry5.get(), entry6.get(),
                       entry7.get(), entry8.get(), entry9.get(), entry10.get(), entry11.get())
