import keyboard
import globalVariables
import browserControl


def listener():
    keyboard.on_press(send_key)
    keyboard.wait()


def send_key(event):
    if event.name in globalVariables.alt_control_key_list:
        browserControl.firefox_window(event.name)
