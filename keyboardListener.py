import keyboard
import globalVariables
import browserControl
from tkinter import messagebox


def listener():
    keyboard.on_press(send_key)
    keyboard.wait()


def send_key(event):
    if event.name in globalVariables.alt_control_key_list:
        browserControl.alt_control_send_keys(event.name)


def set_mini_ftool_shortcut(key_sequence, function):
    try:
        if key_sequence:
            globalVariables.mini_ftool_shortcut = keyboard.add_hotkey(key_sequence, function)
        else:
            if globalVariables.mini_ftool_shortcut:
                keyboard.remove_hotkey(globalVariables.mini_ftool_shortcut)
                globalVariables.mini_ftool_shortcut = None
    except Exception as e:
        messagebox.showerror("Error", "This is not a valid shortcut."
                                      "\n\nError:"
                                      "\n\n" + str(e))


def buffer_shortcut(key_sequence, function):
    try:
        if key_sequence:
            globalVariables.buffer_shortcut = keyboard.add_hotkey(key_sequence, function)
        else:
            if globalVariables.buffer_shortcut:
                keyboard.remove_hotkey(globalVariables.buffer_shortcut)
                globalVariables.buffer_shortcut = None
    except Exception as e:
        messagebox.showerror("Error", "This is not a valid shortcut."
                                      "\n\nError:"
                                      "\n\n" + str(e))
