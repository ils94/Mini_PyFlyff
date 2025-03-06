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


def start_stop_macro_loop():

    global macro_loop_running

    with macro_loop_lock:

        if globalVariables.macro_loop_on:

            globalVariables.macro_loop_on = False

        elif not globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:

            if macro_loop_running:
                return

            globalVariables.macro_loop_on = True

            macro_loop_running = True

            miscs.multithreading(lambda: run_macro_loop())


def run_macro_loop():

    global macro_loop_running

    try:

        macroLoop.macro_loop()

    finally:

        with macro_loop_lock:

            macro_loop_running = False

            globalVariables.macro_loop_on = False


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


def start_stop_buffer():

    global buffer_loop_running

    with buffer_loop_lock:

        if globalVariables.buffer_is_on:

            globalVariables.buffer_is_on = False

        elif not globalVariables.buffer_is_on and globalVariables.buffer_enable_disabled:

            if buffer_loop_running:

                return

            globalVariables.buffer_is_on = True

            buffer_loop_running = True

            miscs.multithreading(lambda: run_buffer_loop())


def run_buffer_loop():

    global buffer_loop_running

    try:

        bufferLoop.buffer_loop()

    finally:

        with buffer_loop_lock:

            buffer_loop_running = False

            globalVariables.buffer_is_on = False


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
