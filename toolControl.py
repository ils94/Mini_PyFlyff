import globalVariables
import bufferLoop
import miscs
import macroLoop


def enable_disable_alt_control(button):
    if globalVariables.alt_controller_on:
        globalVariables.alt_controller_on = False
        button["text"] = "Enable"
    else:
        globalVariables.alt_controller_on = True
        button["text"] = "Disable"


def start_stop_macro_loop(button):
    if globalVariables.macro_loop_on:
        globalVariables.macro_loop_on = False
        button["text"] = "Start"
    elif not globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:
        globalVariables.macro_loop_on = True
        button["text"] = "Stop"
        miscs.multithreading(lambda: macroLoop.macro_loop())


def enable_disable_macro_loop(button):
    if globalVariables.macro_loop_enable_disabled:
        globalVariables.macro_loop_enable_disabled = False
        button["text"] = "Enable"
    else:
        globalVariables.macro_loop_enable_disabled = True
        button["text"] = "Disable"


def enable_disable_buffer(button):
    if globalVariables.buffer_enable_disabled:
        globalVariables.buffer_enable_disabled = False
        button["text"] = "Enable"
    else:
        globalVariables.buffer_enable_disabled = True
        button["text"] = "Disable"


def start_stop_buffer(button, button2, button3):
    if globalVariables.buffer_is_on:
        globalVariables.buffer_is_on = False
        button["text"] = "Start"
    elif not globalVariables.buffer_is_on and globalVariables.buffer_enable_disabled:
        globalVariables.buffer_is_on = True
        button["text"] = "Stop"

        miscs.multithreading(lambda: bufferLoop.buffer_loop(button, button2, button3))
