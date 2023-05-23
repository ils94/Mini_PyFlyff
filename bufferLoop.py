import time
import windowsAPI
import globalVariables
import macroLoop
import miscs

macro_loop_on_check = None

macro_loop_enable_disable_check = None

gt_buffer_check = False


def buffer_loop(button1, button2, button3):
    global macro_loop_on_check
    global gt_buffer_check
    global macro_loop_enable_disable_check

    if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

        macro_loop_on_check = globalVariables.macro_loop_on

        macro_loop_enable_disable_check = globalVariables.macro_loop_enable_disabled

        gt_buffer_check = globalVariables.gt_buffer

        for key in globalVariables.buffer_keys:

            if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

                if macro_loop_on_check:
                    globalVariables.macro_loop_on = False
                    button2["text"] = "Start"

                if macro_loop_enable_disable_check:
                    globalVariables.macro_loop_enable_disabled = False
                    button3["text"] = "Enable"

                if gt_buffer_check:
                    globalVariables.gt_buffer = False

                windowsAPI.windows_api(globalVariables.buffs_hotbar)
                time.sleep(0.5)
                windowsAPI.windows_api(key)

                if globalVariables.buffer_delay:
                    time.sleep(float(globalVariables.buffer_delay))
                else:
                    time.sleep(3)

        globalVariables.buffer_is_going = False

        windowsAPI.windows_api(globalVariables.previous_hotbar)

        globalVariables.buffer_is_on = False

        button1["text"] = "Start"

        if macro_loop_on_check and not globalVariables.macro_loop_on:
            globalVariables.macro_loop_on = True
            button2["text"] = "Stop"

        if macro_loop_enable_disable_check and not globalVariables.macro_loop_enable_disabled:
            globalVariables.macro_loop_enable_disabled = True
            button3["text"] = "Disable"

            if gt_buffer_check and not globalVariables.gt_buffer:
                globalVariables.gt_buffer = True

            miscs.multithreading(lambda: macroLoop.macro_loop())


def gt_buffer():
    while True:
        if globalVariables.gt_buffer:
            windowsAPI.windows_api(globalVariables.gt_buffer_hotbar)
            time.sleep(1)
            windowsAPI.windows_api(globalVariables.gt_buffer_key)

            if globalVariables.gt_buffer_delay:

                time.sleep(float(globalVariables.gt_buffer_delay))
            else:
                time.sleep(45)

        time.sleep(0.5)
