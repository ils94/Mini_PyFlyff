from tkinter import Button, Label, Entry, X, LEFT, RIGHT, LabelFrame, Frame, Checkbutton, IntVar, Menu, END, tix

import globalVariables
import keyboardListener
import os
import saveConfigs
import toolControl
import miscs
import bufferLoop


def gt_checkbutton_state():
    if gt_checkbox_var.get() == 1:
        globalVariables.gt_buffer = True
        miscs.multithreading(lambda: bufferLoop.gt_buffer())
    else:
        globalVariables.gt_buffer = False


def random_delay_checkbutton_state():
    if random_delay_checkbox_var.get() == 1:
        globalVariables.macro_loop_random_delay = 1
    else:
        globalVariables.macro_loop_random_delay = 0


def create_tooltip(widget, text):
    balloon = tix.Balloon(widget, initwait=300)
    balloon.bind_widget(widget, balloonmsg=text)


root = tix.Tk()

menu_bar = Menu(root)

menu = Menu(menu_bar, tearoff=0)

menu.add_command(label="Save Config", command=lambda: saveConfigs.save_key_configs(entry_alt_controller_hotkeys,
                                                                                   entry_macro_loop_hotkey,
                                                                                   entry_macro_loop_delays,
                                                                                   entry_macro_loop_shortcut,
                                                                                   random_delay_checkbox_var.get(),
                                                                                   lambda:
                                                                                   toolControl.start_stop_macro_loop(
                                                                                       button_macro_loop_start_stop),
                                                                                   entry_buffer_hotkeys,
                                                                                   entry_buffs_hotbar,
                                                                                   entry_previous_hotbar,
                                                                                   entry_buffer_delay,
                                                                                   entry_buffer_shortcut,
                                                                                   lambda:
                                                                                   toolControl.start_stop_buffer(
                                                                                       button_buffer_start_stop,
                                                                                       button_macro_loop_start_stop,
                                                                                       button_macro_loop_enable_disable),
                                                                                   entry_GT_hotkey,
                                                                                   entry_GT_delay))

menu_bar.add_cascade(label="Menu", menu=menu)

root.config(menu=menu_bar)

window_width = 262
window_height = 465

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(str(window_width)+"x"+str(window_height)+"+" + str(int(x)) + "+" + str(int(y)))
root.title("Mini PyFlyff")
if os.path.isfile("icon/PyFlyff.ico"):
    root.iconbitmap("icon/PyFlyff.ico")
root.resizable(False, False)

validation_delays = root.register(miscs.validate_input_timers)
validation_keys = root.register(miscs.validate_input_keys)

validation_buffer_delays = root.register(miscs.validate_input_buffer_timer)
validation_buffer_key = root.register(miscs.validate_input_buffer_key)

random_delay_checkbox_var = IntVar()
gt_checkbox_var = IntVar()

label_frame_1 = LabelFrame(root)
label_frame_1.pack(fill=X, padx=2, pady=2)

label_alt_controller = Label(label_frame_1, text="Alt Controller Hotkey(s):")
label_alt_controller.pack(fill=X, padx=1, pady=1)
create_tooltip(label_alt_controller, "Hotkey(s) to control your Alt Client (separate each hotkey(s) with commas).")

entry_alt_controller_hotkeys = Entry(label_frame_1, validate="none")
entry_alt_controller_hotkeys.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_alt_controller_hotkeys, "Hotkey(s) to control your Alt Client (separate each hotkey(s) with commas).")

frame_alt_controller_button = Frame(label_frame_1)
frame_alt_controller_button.pack(fill=X, padx=1, pady=1)

button_alt_controller_enable_disable = Button(frame_alt_controller_button, text="Enable", width=10)
button_alt_controller_enable_disable.pack(side=RIGHT, padx=1, pady=1)
button_alt_controller_enable_disable.config(
    command=lambda: toolControl.enable_disable_alt_control(button_alt_controller_enable_disable))
create_tooltip(button_alt_controller_enable_disable, "Button to Disable/Enable Alt Controller.")

label_frame_2 = LabelFrame(root)
label_frame_2.pack(fill=X, padx=2, pady=2)

label_macro_loop = Label(label_frame_2, text="Macro Loop Key(s):")
label_macro_loop.pack(fill=X, padx=1, pady=1)
create_tooltip(label_macro_loop, "Hotkey(s) for the Macro Loop (separate each hotkey(s) with commas).")

entry_macro_loop_hotkey = Entry(label_frame_2, validate="none")
entry_macro_loop_hotkey.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_macro_loop_hotkey, "Hotkey(s) for the Macro Loop (separate each hotkey(s) with commas).")

label_macro_loop_delays = Label(label_frame_2, text="Macro Loop Delay(s):")
label_macro_loop_delays.pack(fill=X, padx=1, pady=1)
create_tooltip(label_macro_loop_delays,
               "Delay(s) for each hotkey for the Macro Loop (separate each delay(s) with commas).")

entry_macro_loop_delays = Entry(label_frame_2, validate="none")
entry_macro_loop_delays.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_macro_loop_delays,
               "Delay(s) for each hotkey for the Macro Loop (separate each delay(s) with commas).")

label_macro_loop_shortcut = Label(label_frame_2, text="Macro Loop Shortcut:")
label_macro_loop_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(label_macro_loop_shortcut, "Shortcut to Start/Stop the Macro Loop.")

entry_macro_loop_shortcut = Entry(label_frame_2, validate="none")
entry_macro_loop_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_macro_loop_shortcut, "Shortcut to Start/Stop the Macro Loop.")

frame_macro_loop_checkbutton = Frame(label_frame_2)
frame_macro_loop_checkbutton.pack(fill=X, padx=1, pady=1)

checkbutton_macro_loop = Checkbutton(frame_macro_loop_checkbutton, text="Random Delays",
                                     variable=random_delay_checkbox_var, command=random_delay_checkbutton_state)
checkbutton_macro_loop.pack(side=LEFT, padx=1, pady=1)
create_tooltip(checkbutton_macro_loop, "Create random delay(s) for each Macro Loop hotkey(s) interaction.")

frame_macro_loop_buttons = Frame(label_frame_2)
frame_macro_loop_buttons.pack(fill=X, padx=1, pady=1)

button_macro_loop_start_stop = Button(frame_macro_loop_buttons, text="Start", width=10)
button_macro_loop_start_stop.pack(side=LEFT, padx=1, pady=1)
button_macro_loop_start_stop.config(command=lambda: toolControl.start_stop_macro_loop(button_macro_loop_start_stop))
create_tooltip(button_macro_loop_start_stop, "Stop/Start the Macro Loop.")

button_macro_loop_enable_disable = Button(frame_macro_loop_buttons, text="Enable", width=10)
button_macro_loop_enable_disable.pack(side=RIGHT, padx=1, pady=1)
button_macro_loop_enable_disable.config(
    command=lambda: toolControl.enable_disable_macro_loop(button_macro_loop_enable_disable))
create_tooltip(button_macro_loop_enable_disable, "Enable/Disable the Macro Loop.")

label_frame_3 = LabelFrame(root)
label_frame_3.pack(fill=X, padx=2, pady=2)

label_buffer_hotkeys = Label(label_frame_3, text="Buffer Hotkey(s):")
label_buffer_hotkeys.pack(fill=X, padx=1, pady=1)
create_tooltip(label_buffer_hotkeys, "Hotkey(s) for each buff used (separate each hotkey(s) with commas).")

entry_buffer_hotkeys = Entry(label_frame_3, validate="none")
entry_buffer_hotkeys.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_buffer_hotkeys, "Hotkey(s) for each buff used (separate each hotkey(s) with commas).")

frame_buffer_1 = Frame(label_frame_3)
frame_buffer_1.pack(fill=X, padx=1, pady=1)

label_buffs_hotbar = Label(frame_buffer_1, text="Hotbar:")
label_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffs_hotbar, "The hotkey to change to the buff's hotbar.")

entry_buffs_hotbar = Entry(frame_buffer_1, width=5, validate="none")
entry_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffs_hotbar, "The hotkey to change to the buff's hotbar.")

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

label_buffer_shortcut = Label(label_frame_3, text="Buffer Shortcut:")
label_buffer_shortcut.pack(padx=1, pady=1)
create_tooltip(label_buffer_shortcut, "Shortcut to activate the Buffer.")

entry_buffer_shortcut = Entry(label_frame_3, validate="none")
entry_buffer_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_buffer_shortcut, "Shortcut to activate the Buffer.")

frame_buffer_4 = Frame(label_frame_3)
frame_buffer_4.pack(fill=X, padx=1, pady=1)

button_buffer_disable_enable = Button(frame_buffer_4, text="Enable", width=10)
button_buffer_disable_enable.pack(side=RIGHT, padx=1, pady=1)
button_buffer_disable_enable.config(command=lambda: toolControl.enable_disable_buffer(button_buffer_disable_enable))
create_tooltip(button_buffer_disable_enable, "Enable/Disable the Buffer")

button_buffer_start_stop = Button(frame_buffer_4, text="Start", width=10)
button_buffer_start_stop.pack(side=LEFT, padx=1, pady=1)
button_buffer_start_stop.config(
    command=lambda: toolControl.start_stop_buffer(button_buffer_start_stop, button_macro_loop_start_stop,
                                                  button_macro_loop_enable_disable))
create_tooltip(button_buffer_start_stop, "Start/Stop the Buffer")

label_frame_4 = LabelFrame(root)
label_frame_4.pack(fill=X, padx=2, pady=2)

frame_buffer_2 = Frame(label_frame_4)
frame_buffer_2.pack(fill=X, padx=1, pady=1)

checkbutton_gt = Checkbutton(frame_buffer_2, text="Activate GT", variable=gt_checkbox_var, command=gt_checkbutton_state)
checkbutton_gt.pack(side=LEFT, padx=1, pady=1)
create_tooltip(checkbutton_gt, "Mark this box to initiate the GT Buffer.")

label_GT_hotkey = Label(frame_buffer_2, text="GT Key:")
label_GT_hotkey.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_hotkey, "Hotkey to use GT")

entry_GT_hotkey = Entry(frame_buffer_2, width=4, validate="none")
entry_GT_hotkey.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_hotkey, "Hotkey to use GT")

label_GT_delay = Label(frame_buffer_2, text="GT Delay:")
label_GT_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_delay, "Delay to use GT")

entry_GT_delay = Entry(frame_buffer_2, width=5, validate="none")
entry_GT_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_delay, "Delay to use GT")

entry_alt_controller_hotkeys.insert(END, saveConfigs.open_json_config()[0])
entry_macro_loop_hotkey.insert(END, saveConfigs.open_json_config()[1])
entry_macro_loop_delays.insert(END, saveConfigs.open_json_config()[2])
entry_macro_loop_shortcut.insert(END, saveConfigs.open_json_config()[3])
entry_buffer_hotkeys.insert(END, saveConfigs.open_json_config()[5])
entry_buffs_hotbar.insert(END, saveConfigs.open_json_config()[6])
entry_previous_hotbar.insert(END, saveConfigs.open_json_config()[7])
entry_buffer_delay.insert(END, saveConfigs.open_json_config()[8])
entry_buffer_shortcut.insert(END, saveConfigs.open_json_config()[9])
entry_GT_hotkey.insert(END, saveConfigs.open_json_config()[10])
entry_GT_delay.insert(END, saveConfigs.open_json_config()[11])

entry_alt_controller_hotkeys.config(validate="key")
entry_alt_controller_hotkeys.config(validatecommand=(validation_keys, "%S"))

entry_macro_loop_hotkey.config(validate="key")
entry_macro_loop_hotkey.config(validatecommand=(validation_keys, "%S"))

entry_macro_loop_delays.config(validate="key")
entry_macro_loop_delays.config(validatecommand=(validation_delays, "%S"))

entry_buffer_hotkeys.config(validate="key")
entry_buffer_hotkeys.config(validatecommand=(validation_keys, "%S"))

entry_buffs_hotbar.config(validate="key")
entry_buffs_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

entry_previous_hotbar.config(validate="key")
entry_previous_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

entry_buffer_delay.config(validate="key")
entry_buffer_delay.config(validatecommand=(validation_buffer_delays, "%S"))

entry_GT_hotkey.config(validate="key")
entry_GT_hotkey.config(validatecommand=(validation_buffer_key, "%S"))

entry_GT_delay.config(validate="key")
entry_GT_delay.config(validatecommand=(validation_buffer_delays, "%S"))

random_delay_checkbox_var.set(int(saveConfigs.open_json_config()[4]))

globalVariables.macro_loop_random_delay = int(saveConfigs.open_json_config()[4])

miscs.multithreading(keyboardListener.listener)

root.mainloop()
