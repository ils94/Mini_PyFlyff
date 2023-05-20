from tkinter import Tk, Button, Label, Entry, X, LEFT, RIGHT, Frame, Checkbutton, IntVar, Menu, END
import miscs
import globalVariables
import keyboardListener
import miniFtool
import helpWindow
import os
import saveConfigs


def start_stop_alt_control():
    if globalVariables.alt_control_on:
        globalVariables.alt_control_on = False
        button_alt_control_start_stop["text"] = "Enable"
    else:
        globalVariables.alt_control_on = True
        button_alt_control_start_stop["text"] = "Disable"


def start_stop_mini_ftool():
    if globalVariables.mini_ftool_on:
        globalVariables.mini_ftool_on = False
        button_mini_ftool_start_stop["text"] = "Start"
    else:
        globalVariables.mini_ftool_on = True
        button_mini_ftool_start_stop["text"] = "Stop"


def save_mini_ftool_key():
    globalVariables.mini_ftool_keys = entry_mini_ftool_key.get().split(",")
    globalVariables.mini_ftool_key_timers = entry_mini_ftool_timers.get().split(",")

    saveConfigs.save_config(entry_alt_control_keys.get(), entry_mini_ftool_key.get(), entry_mini_ftool_timers.get(),
                            checkbox_var.get())


def save_keys():
    globalVariables.alt_control_key_list = entry_alt_control_keys.get().split(",")
    saveConfigs.save_config(entry_alt_control_keys.get(), entry_mini_ftool_key.get(), entry_mini_ftool_timers.get(),
                            checkbox_var.get())


def validate_input_timers(char):
    if char.isdigit() or char == "," or char == ".":
        return True
    else:
        return False


def validate_input_keys(char):
    if char.isalnum() or char == ",":
        return True
    else:
        return False


root = Tk()

menu_bar = Menu(root)

menu = Menu(menu_bar, tearoff=0)

menu.add_command(label="Help", command=lambda: helpWindow.open_help())

menu_bar.add_cascade(label="Menu", menu=menu)

root.config(menu=menu_bar)

window_width = 250
window_height = 220

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("250x220+" + str(int(x)) + "+" + str(int(y)))
root.title("Mini PyFlyff")
if os.path.isfile("icon/PyFlyff.ico"):
    root.iconbitmap("icon/PyFlyff.ico")
root.resizable(False, False)

validation_timers = root.register(validate_input_timers)
validation_keys = root.register(validate_input_keys)

checkbox_var = IntVar()

label_alt_control = Label(text="Alt Control Key(s):")
label_alt_control.pack(fill=X, padx=1, pady=1)

entry_alt_control_keys = Entry(validate="none")
entry_alt_control_keys.pack(fill=X, padx=1, pady=1)

frame_alt_control_save_button = Frame(root)
frame_alt_control_save_button.pack(fill=X, padx=1, pady=1)

button_alt_control_save = Button(frame_alt_control_save_button, text="Save key(s)", width=10, command=save_keys)
button_alt_control_save.pack(side=LEFT, padx=1, pady=1)

button_alt_control_start_stop = Button(frame_alt_control_save_button, text="Enable", width=10,
                                       command=start_stop_alt_control)
button_alt_control_start_stop.pack(side=RIGHT, padx=1, pady=1)

label_mini_ftool = Label(text="Mini Ftool Key(s):")
label_mini_ftool.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_key = Entry(validate="none")
entry_mini_ftool_key.pack(fill=X, padx=1, pady=1)

label_mini_ftool_timers = Label(text="Mini Ftool Key(s) Timers:")
label_mini_ftool_timers.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_timers = Entry(validate="none")
entry_mini_ftool_timers.pack(fill=X, padx=1, pady=1)

frame_mini_ftool_checkbutton = Frame(root)
frame_mini_ftool_checkbutton.pack(fill=X, padx=1, pady=1)

checkbutton_mini_ftool = Checkbutton(frame_mini_ftool_checkbutton, text="Make Timers Random", variable=checkbox_var)
checkbutton_mini_ftool.pack(side=LEFT, padx=1, pady=1)

frame_mini_ftool_buttons = Frame(root)
frame_mini_ftool_buttons.pack(fill=X, padx=1, pady=1)

button_mini_ftool_save = Button(frame_mini_ftool_buttons, text="Save Key(s)", width=10, command=save_mini_ftool_key)
button_mini_ftool_save.pack(side=LEFT, padx=1, pady=1)

button_mini_ftool_start_stop = Button(frame_mini_ftool_buttons, text="Start", width=10,
                                      command=start_stop_mini_ftool)
button_mini_ftool_start_stop.pack(side=RIGHT, padx=1, pady=1)

entry_alt_control_keys.insert(END, saveConfigs.open_config()[0])
entry_mini_ftool_key.insert(END, saveConfigs.open_config()[1])
entry_mini_ftool_timers.insert(END, saveConfigs.open_config()[2])

entry_alt_control_keys.config(validate="key")
entry_alt_control_keys.config(validatecommand=(validation_keys, "%S"))

entry_mini_ftool_key.config(validate="key")
entry_mini_ftool_key.config(validatecommand=(validation_keys, "%S"))

entry_mini_ftool_timers.config(validate="key")
entry_mini_ftool_timers.config(validatecommand=(validation_timers, "%S"))

checkbox_var.set(int(saveConfigs.open_config()[3]))

miscs.multithreading(keyboardListener.listener)

miscs.multithreading(lambda: miniFtool.mini_ftool(checkbox_var.get()))

root.mainloop()
