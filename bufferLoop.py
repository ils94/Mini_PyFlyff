import time
import windowsAPI
import globalVariables
import toolControl

macro_loop_check = False

gt_buffer_check = False


def buffer_loop(button, button2):
    global macro_loop_check
    global gt_buffer_check

    if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

        for key in globalVariables.buffer_keys:

            if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

                if globalVariables.macro_loop_on:
                    macro_loop_check = True
                    toolControl.start_stop_macro_loop(button2)

                if globalVariables.gt_buffer:
                    gt_buffer_check = True
                    globalVariables.gt_buffer = False

                windowsAPI.windows_api(globalVariables.buffs_hotbar)
                time.sleep(0.5)
                windowsAPI.windows_api(key)

                if globalVariables.buffer_delay:
                    time.sleep(float(globalVariables.buffer_delay))
                else:
                    time.sleep(3)

        if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

            if macro_loop_check:
                toolControl.start_stop_macro_loop(button2)

            if gt_buffer_check:
                globalVariables.gt_buffer = True

        globalVariables.buffer_is_going = False

        windowsAPI.windows_api(globalVariables.previous_hotbar)

        globalVariables.buffer_is_on = False

        button["text"] = "Start"


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
