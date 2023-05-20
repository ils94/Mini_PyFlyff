import globalVariables


def start_stop_alt_control(button):
    if globalVariables.alt_control_on:
        globalVariables.alt_control_on = False
        button["text"] = "Enable"
    else:
        globalVariables.alt_control_on = True
        button["text"] = "Disable"


def start_stop_mini_ftool(button):
    if globalVariables.mini_ftool_on:
        globalVariables.mini_ftool_on = False
        button["text"] = "Start"
    else:
        globalVariables.mini_ftool_on = True
        button["text"] = "Stop"
