import time
import windowsAPI
import globalVariables
import toolControl

mini_ftool_check = False

gt_buffer_check = False


def buffer_loop(button, button2):
    global mini_ftool_check
    global gt_buffer_check

    if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

        for key in globalVariables.buffer_keys:

            if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

                if globalVariables.macro_loop_enable_disabled:
                    mini_ftool_check = True
                    toolControl.enable_disable_mini_ftool(button2)

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

            if mini_ftool_check:
                toolControl.enable_disable_mini_ftool(button2)

            if gt_buffer_check:
                globalVariables.gt_buffer = True

        globalVariables.buffer_is_going = False

        windowsAPI.windows_api(globalVariables.previous_hotbar)

        globalVariables.buffer_is_on = False

        button["text"] = "Start"


def gt_buffer():
    while True:
        if globalVariables.gt_buffer and globalVariables.gt_buffer_delay:
            windowsAPI.windows_api(globalVariables.gt_buffer_hotbar)
            time.sleep(1)
            windowsAPI.windows_api(globalVariables.gt_buffer_key)

            time.sleep(float(globalVariables.gt_buffer_delay))

        time.sleep(0.5)
