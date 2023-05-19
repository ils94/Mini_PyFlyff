from tkinter import Tk, Button, Label, Entry, X, LEFT, RIGHT, Frame, Checkbutton, IntVar
import keyboard
import threading
import win32api
import win32con
import win32gui
import virtualKeys
import time
import random

on = False

alt_control_key_list = []

mini_ftool_keys = []

mini_ftool_key_timers = []


def multithreading(function):
    t = threading.Thread(target=function)
    t.setDaemon(True)
    t.start()


def start_mini_ftool():
    global on

    if on:
        on = False
    else:
        on = True


def save_mini_ftool_key():
    global mini_ftool_keys
    global mini_ftool_key_timers

    mini_ftool_keys = entry_mini_ftool_key.get().split(",")
    mini_ftool_key_timers = entry_mini_ftool_timers.get().split(",")


def mini_ftool():
    global on
    global mini_ftool_keys
    global mini_ftool_key_timers

    while True:
        if on:
            for key, timer in zip(mini_ftool_keys, mini_ftool_key_timers):
                if on:
                    firefox_window(key)

                    if checkbox_var.get() == 1:
                        time.sleep(random.uniform(0, float(timer)))
                    else:
                        time.sleep(int(timer))

        time.sleep(1)


def save_keys():
    global alt_control_key_list
    alt_control_key_list = entry_alt_control_keys.get().split(",")


def listener():
    keyboard.on_press(send_key)
    keyboard.wait()


def firefox_window(key):
    window = win32gui.FindWindow("MozillaWindowClass", None)
    win32api.SendMessage(window, win32con.WM_KEYDOWN, virtualKeys.vk_code.get(key), 0)
    time.sleep(0.1)
    win32api.SendMessage(window, win32con.WM_KEYUP, virtualKeys.vk_code.get(key), 0)


def send_key(event):
    print(event.name)
    if event.name in alt_control_key_list:
        firefox_window(event.name)


root = Tk()
root.geometry("250x225")
root.title("Mini PyFlyff")
root.resizable(False, False)

checkbox_var = IntVar()

label_alt_control = Label(text="Alt Control Key(s):")
label_alt_control.pack(fill=X, padx=1, pady=1)

entry_alt_control_keys = Entry()
entry_alt_control_keys.pack(fill=X, padx=1, pady=1)

frame_alt_control_save_button = Frame(root)
frame_alt_control_save_button.pack(fill=X, padx=1, pady=1)

button_alt_control_save = Button(frame_alt_control_save_button, text="Save key(s)", command=save_keys)
button_alt_control_save.pack(side=LEFT, padx=1, pady=1)

label_mini_ftool = Label(text="Mini Ftool Key(s):")
label_mini_ftool.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_key = Entry()
entry_mini_ftool_key.pack(fill=X, padx=1, pady=1)

label_mini_ftool_timers = Label(text="Mini Ftool Key(s) Timers:")
label_mini_ftool_timers.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_timers = Entry()
entry_mini_ftool_timers.pack(fill=X, padx=1, pady=1)

frame_mini_ftool_checkbutton = Frame(root)
frame_mini_ftool_checkbutton.pack(fill=X, padx=1, pady=1)

checkbutton_mini_ftool = Checkbutton(frame_mini_ftool_checkbutton, text="Make Timers Random", variable=checkbox_var)
checkbutton_mini_ftool.pack(side=LEFT, padx=1, pady=1)

frame_mini_ftool_buttons = Frame(root)
frame_mini_ftool_buttons.pack(fill=X, padx=1, pady=1)

button_mini_ftool_save = Button(frame_mini_ftool_buttons, text="Save Key(s)", command=save_mini_ftool_key)
button_mini_ftool_save.pack(side=LEFT, padx=1, pady=1)

button_mini_ftool_start_stop = Button(frame_mini_ftool_buttons, text="Start/Stop", command=start_mini_ftool)
button_mini_ftool_start_stop.pack(side=RIGHT, padx=1, pady=1)

multithreading(listener)

multithreading(mini_ftool)

root.mainloop()
