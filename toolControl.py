import globalVariables


def start_stop_alt_control(button):
    if globalVariables.alt_control_on:
        globalVariables.alt_control_on = False
        button["text"] = "Enable"
    else:
        globalVariables.alt_control_on = True
        button["text"] = "Disable"


def start_stop_mini_ftool(button):
    if globalVariables.macro_loop_on:
        globalVariables.macro_loop_on = False
        button["text"] = "Start"
    else:
        globalVariables.macro_loop_on = True
        button["text"] = "Stop"


def enable_disable_mini_ftool(button):
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
