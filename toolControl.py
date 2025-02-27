import globalVariables
import bufferLoop
import miscs
import macroLoop
import threading

macro_loop_running = False
buffer_loop_running = False
gt_buffer_running = False

macro_loop_lock = threading.Lock()
buffer_loop_lock = threading.Lock()
gt_buffer_lock = threading.Lock()


def enable_disable_alt_control(button):
    if globalVariables.alt_controller_on:
        globalVariables.alt_controller_on = False
        button["text"] = "Enable"
    else:
        globalVariables.alt_controller_on = True
        button["text"] = "Disable"


def start_stop_macro_loop(button):
    global macro_loop_running

    with macro_loop_lock:
        if globalVariables.macro_loop_on:
            globalVariables.macro_loop_on = False
            button["text"] = "Start"
        elif not globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:
            if macro_loop_running:
                return

            globalVariables.macro_loop_on = True
            button["text"] = "Stop"
            macro_loop_running = True
            miscs.multithreading(lambda: run_macro_loop(button))


def run_macro_loop(button):
    global macro_loop_running

    try:
        macroLoop.macro_loop()
    finally:
        with macro_loop_lock:
            macro_loop_running = False
            globalVariables.macro_loop_on = False
            button["text"] = "Start"


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
    global buffer_loop_running

    with buffer_loop_lock:
        if globalVariables.buffer_is_on:
            globalVariables.buffer_is_on = False
            button["text"] = "Start"
        elif not globalVariables.buffer_is_on and globalVariables.buffer_enable_disabled:
            if buffer_loop_running:
                return

            globalVariables.buffer_is_on = True
            button["text"] = "Stop"
            buffer_loop_running = True
            miscs.multithreading(lambda: run_buffer_loop(button, button2, button3))


def run_buffer_loop(button, button2, button3):
    global buffer_loop_running

    try:
        bufferLoop.buffer_loop(button, button2, button3)
    finally:
        with buffer_loop_lock:
            buffer_loop_running = False
            globalVariables.buffer_is_on = False
            button["text"] = "Start"


def gt_checkbutton_state(gt_checkbox_var):
    global gt_buffer_running

    with gt_buffer_lock:
        if gt_checkbox_var.get() == 1:
            if gt_buffer_running:
                print("GT Buffer is already running!")
                return

            globalVariables.gt_buffer = True
            gt_buffer_running = True
            miscs.multithreading(lambda: run_gt_buffer())
        else:
            globalVariables.gt_buffer = False


def run_gt_buffer():
    global gt_buffer_running

    try:
        bufferLoop.gt_buffer()
    finally:
        with gt_buffer_lock:
            gt_buffer_running = False
