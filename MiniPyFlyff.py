from tkinter import Button, Label, Entry, X, LEFT, RIGHT, Frame, Checkbutton, IntVar, Menu, END, tix

import keyboardListener
import miniFtool
import helpWindow
import os
import saveConfigs
import toolControl
import miscs
import bufferLoop


def create_tooltip(widget, text):
    balloon = tix.Balloon(widget)
    balloon.bind_widget(widget, balloonmsg=text)


root = tix.Tk()

menu_bar = Menu(root)

menu = Menu(menu_bar, tearoff=0)

menu.add_command(label="Help", command=lambda: helpWindow.open_help())

menu.add_command(label="Save Keys", command=lambda: saveConfigs.save_key_configs(entry_alt_control_keys,
                                                                                 entry_mini_ftool_key,
                                                                                 entry_mini_ftool_timers,
                                                                                 entry_mini_ftool_shortcut,
                                                                                 checkbox_var.get(),
                                                                                 lambda:
                                                                                 toolControl.start_stop_mini_ftool(
                                                                                     button_mini_ftool_start_stop),
                                                                                 entry_buffer,
                                                                                 entry_buffs_hotbar,
                                                                                 entry_previous_hotbar,
                                                                                 entry_buffer_timer,
                                                                                 entry_buffer_shortcut,
                                                                                 lambda:
                                                                                 toolControl.enable_disable_buffer(
                                                                                     button_buffer_disable_enable)))

menu_bar.add_cascade(label="Menu", menu=menu)

root.config(menu=menu_bar)

window_width = 250
window_height = 265

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("250x400+" + str(int(x)) + "+" + str(int(y)))
root.title("Mini PyFlyff")
if os.path.isfile("icon/PyFlyff.ico"):
    root.iconbitmap("icon/PyFlyff.ico")
root.resizable(False, False)

validation_timers = root.register(miscs.validate_input_timers)
validation_keys = root.register(miscs.validate_input_keys)

validation_buffer_timer = root.register(miscs.validate_input_buffer_timer)
validation_buffer_key = root.register(miscs.validate_input_buffer_key)

checkbox_var = IntVar()

label_alt_control = Label(text="Alt Control Key(s):")
label_alt_control.pack(fill=X, padx=1, pady=1)

entry_alt_control_keys = Entry(validate="none")
entry_alt_control_keys.pack(fill=X, padx=1, pady=1)

frame_alt_control_save_button = Frame(root)
frame_alt_control_save_button.pack(fill=X, padx=1, pady=1)

button_alt_control_start_stop = Button(frame_alt_control_save_button, text="Enable", width=10)
button_alt_control_start_stop.pack(side=RIGHT, padx=1, pady=1)
button_alt_control_start_stop.config(command=lambda: toolControl.start_stop_alt_control(button_alt_control_start_stop))

label_mini_ftool = Label(text="Mini Ftool Key(s):")
label_mini_ftool.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_key = Entry(validate="none")
entry_mini_ftool_key.pack(fill=X, padx=1, pady=1)

label_mini_ftool_timers = Label(text="Mini Ftool Key(s) Timers:")
label_mini_ftool_timers.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_timers = Entry(validate="none")
entry_mini_ftool_timers.pack(fill=X, padx=1, pady=1)

label_mini_ftool_shortcut = Label(text="Mini Ftool Shortcut:")
label_mini_ftool_shortcut.pack(fill=X, padx=1, pady=1)

entry_mini_ftool_shortcut = Entry(validate="none")
entry_mini_ftool_shortcut.pack(fill=X, padx=1, pady=1)

frame_mini_ftool_checkbutton = Frame(root)
frame_mini_ftool_checkbutton.pack(fill=X, padx=1, pady=1)

checkbutton_mini_ftool = Checkbutton(frame_mini_ftool_checkbutton, text="Make Timers Random", variable=checkbox_var)
checkbutton_mini_ftool.pack(side=LEFT, padx=1, pady=1)

frame_mini_ftool_buttons = Frame(root)
frame_mini_ftool_buttons.pack(fill=X, padx=1, pady=1)

button_mini_ftool_start_stop = Button(frame_mini_ftool_buttons, text="Start", width=10)
button_mini_ftool_start_stop.pack(side=LEFT, padx=1, pady=1)
button_mini_ftool_start_stop.config(command=lambda: toolControl.start_stop_mini_ftool(button_mini_ftool_start_stop))

button_mini_ftool_enable_disable = Button(frame_mini_ftool_buttons, text="Enable", width=10)
button_mini_ftool_enable_disable.pack(side=RIGHT, padx=1, pady=1)
button_mini_ftool_enable_disable.config(
    command=lambda: toolControl.enable_disable_mini_ftool(button_mini_ftool_enable_disable))

label_buffer = Label(text="Buffer Key(s):")
label_buffer.pack(fill=X, padx=1, pady=1)

entry_buffer = Entry(validate="none")
entry_buffer.pack(fill=X, padx=1, pady=1)

frame_buffer = Frame(root)
frame_buffer.pack(fill=X, padx=1, pady=1)

label_buffs_hotbar = Label(frame_buffer, text="B. Hotbar:")
label_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffs_hotbar, "Buffs Hotbar: The hotkey for the hotbar where your buffs are.")

entry_buffs_hotbar = Entry(frame_buffer, width=2, validate="none")
entry_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffs_hotbar, "Buffs Hotbar: The hotkey for the hotbar where your buffs are.")

label_preview_hotbar = Label(frame_buffer, text="P. Hotbar:")
label_preview_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_preview_hotbar, "Previous Hotbar: The hotkey to go back to the previous hotbar.")

entry_previous_hotbar = Entry(frame_buffer, width=2, validate="none")
entry_previous_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_previous_hotbar, "Previous Hotbar: The hotkey to go back to the previous hotbar.")

label_buffer_timer = Label(frame_buffer, text="B. Timer:")
label_buffer_timer.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffer_timer, "Buffer Timer: Delay for the buffer to rebuff your character (Optional).")

entry_buffer_timer = Entry(frame_buffer, width=10, validate="none")
entry_buffer_timer.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffer_timer, "Buffer Timer: Delay for the buffer to rebuff your character (Optional).")

frame_buffer_2 = Frame(root)
frame_buffer_2.pack(fill=X, padx=1, pady=1)

label_buffer_shortcut = Label(frame_buffer_2, text="Buffer Shortcut:")
label_buffer_shortcut.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffer_shortcut, "Buffer Shortcut: Shortcut to activate the Buffer.")

entry_buffer_shortcut = Entry(frame_buffer_2, validate="none")
entry_buffer_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_buffer_shortcut, "Buffer Shortcut: Shortcut to activate the Buffer.")

frame_buffer_3 = Frame(root)
frame_buffer_3.pack(fill=X, padx=1, pady=1)

button_buffer_disable_enable = Button(frame_buffer_3, text="Enable", width=10)
button_buffer_disable_enable.pack(side=RIGHT, padx=1, pady=1)
button_buffer_disable_enable.config(command=lambda: toolControl.enable_disable_buffer(button_buffer_disable_enable))

entry_alt_control_keys.insert(END, saveConfigs.open_json_config()[0])
entry_mini_ftool_key.insert(END, saveConfigs.open_json_config()[1])
entry_mini_ftool_timers.insert(END, saveConfigs.open_json_config()[2])
entry_mini_ftool_shortcut.insert(END, saveConfigs.open_json_config()[3])
entry_buffer.insert(END, saveConfigs.open_json_config()[5])
entry_buffs_hotbar.insert(END, saveConfigs.open_json_config()[6])
entry_previous_hotbar.insert(END, saveConfigs.open_json_config()[7])
entry_buffer_timer.insert(END, saveConfigs.open_json_config()[8])
entry_buffer_shortcut.insert(END, saveConfigs.open_json_config()[9])

entry_alt_control_keys.config(validate="key")
entry_alt_control_keys.config(validatecommand=(validation_keys, "%S"))

entry_mini_ftool_key.config(validate="key")
entry_mini_ftool_key.config(validatecommand=(validation_keys, "%S"))

entry_mini_ftool_timers.config(validate="key")
entry_mini_ftool_timers.config(validatecommand=(validation_timers, "%S"))

entry_buffer.config(validate="key")
entry_buffer.config(validatecommand=(validation_keys, "%S"))

entry_buffs_hotbar.config(validate="key")
entry_buffs_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

entry_previous_hotbar.config(validate="key")
entry_previous_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

entry_buffer_timer.config(validate="key")
entry_buffer_timer.config(validatecommand=(validation_buffer_timer, "%S"))

checkbox_var.set(int(saveConfigs.open_json_config()[4]))

miscs.multithreading(keyboardListener.listener)

miscs.multithreading(lambda: miniFtool.mini_ftool(checkbox_var.get()))

miscs.multithreading(lambda: bufferLoop.buffer_loop(button_mini_ftool_enable_disable))

miscs.multithreading(lambda: bufferLoop.gt_buffer())

root.mainloop()
