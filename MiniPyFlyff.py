from tkinter import Button, Label, Entry, X, LEFT, RIGHT, Frame, Checkbutton, IntVar, Menu, END, tix

import globalVariables
import keyboardListener
import macroLoop
import helpWindow
import os
import saveConfigs
import toolControl
import miscs
import bufferLoop


def gt_checkbutton_state():
    if checkbox_var_2.get() == 1:
        globalVariables.gt_buffer = True
    else:
        globalVariables.gt_buffer = False


def create_tooltip(widget, text):
    balloon = tix.Balloon(widget)
    balloon.bind_widget(widget, balloonmsg=text)


root = tix.Tk()

menu_bar = Menu(root)

menu = Menu(menu_bar, tearoff=0)

menu.add_command(label="Help", command=lambda: helpWindow.open_help())

menu.add_command(label="Save Keys", command=lambda: saveConfigs.save_key_configs(entry_alt_control_keys,
                                                                                 entry_macro_loop_key,
                                                                                 entry_macro_loop_timers,
                                                                                 entry_macro_loop_shortcut,
                                                                                 checkbox_var.get(),
                                                                                 lambda:
                                                                                 toolControl.start_stop_mini_ftool(
                                                                                     button_macro_loop_start_stop),
                                                                                 entry_buffer,
                                                                                 entry_buffs_hotbar,
                                                                                 entry_previous_hotbar,
                                                                                 entry_buffer_delay,
                                                                                 entry_buffer_shortcut,
                                                                                 lambda:
                                                                                 toolControl.start_stop_buffer(
                                                                                     button_buffer_start_stop,
                                                                                     button_macro_loop_enable_disable),
                                                                                 entry_GT_key,
                                                                                 entry_GT_timer))

menu_bar.add_cascade(label="Menu", menu=menu)

root.config(menu=menu_bar)

window_width = 260
window_height = 430

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry("260x430+" + str(int(x)) + "+" + str(int(y)))
root.title("Mini PyFlyff")
if os.path.isfile("icon/PyFlyff.ico"):
    root.iconbitmap("icon/PyFlyff.ico")
root.resizable(False, False)

validation_timers = root.register(miscs.validate_input_timers)
validation_keys = root.register(miscs.validate_input_keys)

validation_buffer_timer = root.register(miscs.validate_input_buffer_timer)
validation_buffer_key = root.register(miscs.validate_input_buffer_key)

checkbox_var = IntVar()
checkbox_var_2 = IntVar()

label_alt_control = Label(text="Alt Control Key(s):")
label_alt_control.pack(fill=X, padx=1, pady=1)

entry_alt_control_keys = Entry(validate="none")
entry_alt_control_keys.pack(fill=X, padx=1, pady=1)

frame_alt_control_save_button = Frame(root)
frame_alt_control_save_button.pack(fill=X, padx=1, pady=1)

button_alt_control_start_stop = Button(frame_alt_control_save_button, text="Enable", width=10)
button_alt_control_start_stop.pack(side=RIGHT, padx=1, pady=1)
button_alt_control_start_stop.config(
    command=lambda: toolControl.enable_disable_alt_control(button_alt_control_start_stop))

label_macro_loop = Label(text="Macro Loop Key(s):")
label_macro_loop.pack(fill=X, padx=1, pady=1)

entry_macro_loop_key = Entry(validate="none")
entry_macro_loop_key.pack(fill=X, padx=1, pady=1)

label_macro_loop_timers = Label(text="Macro Loop Delay(s):")
label_macro_loop_timers.pack(fill=X, padx=1, pady=1)

entry_macro_loop_timers = Entry(validate="none")
entry_macro_loop_timers.pack(fill=X, padx=1, pady=1)

label_macro_loop_shortcut = Label(text="Macro Loop Shortcut:")
label_macro_loop_shortcut.pack(fill=X, padx=1, pady=1)

entry_macro_loop_shortcut = Entry(validate="none")
entry_macro_loop_shortcut.pack(fill=X, padx=1, pady=1)

frame_macro_loop_checkbutton = Frame(root)
frame_macro_loop_checkbutton.pack(fill=X, padx=1, pady=1)

checkbutton_macro_loop = Checkbutton(frame_macro_loop_checkbutton, text="Random Delays", variable=checkbox_var)
checkbutton_macro_loop.pack(side=LEFT, padx=1, pady=1)

frame_macro_loop_buttons = Frame(root)
frame_macro_loop_buttons.pack(fill=X, padx=1, pady=1)

button_macro_loop_start_stop = Button(frame_macro_loop_buttons, text="Start", width=10)
button_macro_loop_start_stop.pack(side=LEFT, padx=1, pady=1)
button_macro_loop_start_stop.config(command=lambda: toolControl.start_stop_mini_ftool(button_macro_loop_start_stop))

button_macro_loop_enable_disable = Button(frame_macro_loop_buttons, text="Enable", width=10)
button_macro_loop_enable_disable.pack(side=RIGHT, padx=1, pady=1)
button_macro_loop_enable_disable.config(
    command=lambda: toolControl.enable_disable_mini_ftool(button_macro_loop_enable_disable))

label_buffer = Label(text="Buffer Key(s):")
label_buffer.pack(fill=X, padx=1, pady=1)

entry_buffer = Entry(validate="none")
entry_buffer.pack(fill=X, padx=1, pady=1)

frame_buffer_1 = Frame(root)
frame_buffer_1.pack(fill=X, padx=1, pady=1)

label_buffs_hotbar = Label(frame_buffer_1, text="Hotbar:")
label_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffs_hotbar, "The hotkey for the hotbar where your buffs are.")

entry_buffs_hotbar = Entry(frame_buffer_1, width=5, validate="none")
entry_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffs_hotbar, "The hotkey for the hotbar where your buffs are.")

label_preview_hotbar = Label(frame_buffer_1, text="Previous:")
label_preview_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_preview_hotbar, "The hotkey to go back to the previous hotbar.")

entry_previous_hotbar = Entry(frame_buffer_1, width=5, validate="none")
entry_previous_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_previous_hotbar, "The hotkey to go back to the previous hotbar.")

label_buffer_delay = Label(frame_buffer_1, text="Delay:")
label_buffer_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffer_delay, "Delay to cast each buff.")

entry_buffer_delay = Entry(frame_buffer_1, width=6, validate="none")
entry_buffer_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffer_delay, "Delay to cast each buff.")

label_buffer_shortcut = Label(text="Buffer Shortcut:")
label_buffer_shortcut.pack(padx=1, pady=1)
create_tooltip(label_buffer_shortcut, "Shortcut to activate the Buffer.")

entry_buffer_shortcut = Entry(validate="none")
entry_buffer_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_buffer_shortcut, "Shortcut to activate the Buffer.")

frame_buffer_4 = Frame(root)
frame_buffer_4.pack(fill=X, padx=1, pady=1)

button_buffer_disable_enable = Button(frame_buffer_4, text="Enable", width=10)
button_buffer_disable_enable.pack(side=RIGHT, padx=1, pady=1)
button_buffer_disable_enable.config(command=lambda: toolControl.enable_disable_buffer(button_buffer_disable_enable))

button_buffer_start_stop = Button(frame_buffer_4, text="Start", width=10)
button_buffer_start_stop.pack(side=LEFT, padx=1, pady=1)
button_buffer_start_stop.config(
    command=lambda: toolControl.start_stop_buffer(button_buffer_start_stop, button_macro_loop_enable_disable))

frame_buffer_2 = Frame(root)
frame_buffer_2.pack(fill=X, padx=1, pady=1)

checkbutton_gt = Checkbutton(frame_buffer_2, text="GT", variable=checkbox_var_2, command=gt_checkbutton_state)
checkbutton_gt.pack(side=LEFT, padx=1, pady=1)

label_GT_key = Label(frame_buffer_2, text="Key:")
label_GT_key.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_key, "Key to use GT")

entry_GT_key = Entry(frame_buffer_2, width=4, validate="none")
entry_GT_key.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_key, "Key to use GT")

label_GT_hotbar = Label(frame_buffer_2, text="Hotbar:")
label_GT_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_hotbar, "The hotbar where your GT is.")

entry_GT_hotbar = Entry(frame_buffer_2, width=4, validate="none")
entry_GT_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_hotbar, "The hotbar where your GT is.")

label_GT_timer = Label(frame_buffer_2, text="Delay:")
label_GT_timer.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_timer, "Delay to use GT")

entry_GT_timer = Entry(frame_buffer_2, width=5, validate="none")
entry_GT_timer.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_timer, "Delay to use GT")

entry_alt_control_keys.insert(END, saveConfigs.open_json_config()[0])
entry_macro_loop_key.insert(END, saveConfigs.open_json_config()[1])
entry_macro_loop_timers.insert(END, saveConfigs.open_json_config()[2])
entry_macro_loop_shortcut.insert(END, saveConfigs.open_json_config()[3])
entry_buffer.insert(END, saveConfigs.open_json_config()[5])
entry_buffs_hotbar.insert(END, saveConfigs.open_json_config()[6])
entry_previous_hotbar.insert(END, saveConfigs.open_json_config()[7])
entry_buffer_delay.insert(END, saveConfigs.open_json_config()[8])
entry_buffer_shortcut.insert(END, saveConfigs.open_json_config()[9])
entry_GT_key.insert(END, saveConfigs.open_json_config()[10])
entry_GT_timer.insert(END, saveConfigs.open_json_config()[11])

entry_alt_control_keys.config(validate="key")
entry_alt_control_keys.config(validatecommand=(validation_keys, "%S"))

entry_macro_loop_key.config(validate="key")
entry_macro_loop_key.config(validatecommand=(validation_keys, "%S"))

entry_macro_loop_timers.config(validate="key")
entry_macro_loop_timers.config(validatecommand=(validation_timers, "%S"))

entry_buffer.config(validate="key")
entry_buffer.config(validatecommand=(validation_keys, "%S"))

entry_buffs_hotbar.config(validate="key")
entry_buffs_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

entry_previous_hotbar.config(validate="key")
entry_previous_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

entry_buffer_delay.config(validate="key")
entry_buffer_delay.config(validatecommand=(validation_buffer_timer, "%S"))

entry_GT_key.config(validate="key")
entry_GT_key.config(validatecommand=(validation_buffer_key, "%S"))

entry_GT_timer.config(validate="key")
entry_GT_timer.config(validatecommand=(validation_buffer_timer, "%S"))

checkbox_var.set(int(saveConfigs.open_json_config()[4]))

miscs.multithreading(keyboardListener.listener)

miscs.multithreading(lambda: macroLoop.macro_loop(checkbox_var.get()))

miscs.multithreading(lambda: bufferLoop.gt_buffer())

root.mainloop()
