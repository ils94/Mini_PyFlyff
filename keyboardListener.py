import keyboard
import globalVariables
import altController
from tkinter import messagebox


def listener():
    keyboard.on_press(send_key)

    keyboard.wait()


def send_key(event):
    if event.name in globalVariables.alt_controller_hotkey_list:
        altController.alt_control_send_keys(event.name)


def set_macro_loop_shortcut(key_sequence, function):
    try:

        if key_sequence:

            globalVariables.macro_loop_shortcut = keyboard.add_hotkey(key_sequence, function)

        else:

            if globalVariables.macro_loop_shortcut:
                keyboard.remove_hotkey(globalVariables.macro_loop_shortcut)

                globalVariables.macro_loop_shortcut = None

    except Exception as e:

        messagebox.showerror("Error", f"This is not a valid shortcut\n\n{str(e)}")


def set_buffer_shortcut(key_sequence, function):
    try:

        if key_sequence:

            globalVariables.buffer_shortcut = keyboard.add_hotkey(key_sequence, function)

        else:

            if globalVariables.buffer_shortcut:
                keyboard.remove_hotkey(globalVariables.buffer_shortcut)

                globalVariables.buffer_shortcut = None

    except Exception as e:

        messagebox.showerror("Error", f"This is not a valid shortcut\n\n{str(e)}")
