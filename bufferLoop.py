import time
import windowsAPI
import globalVariables
import toolControl

mini_ftool_check = False

gt_buffer_check = False


def buffer_loop(button):
    global mini_ftool_check
    global gt_buffer_check

    for key in globalVariables.buffer_keys:

        if globalVariables.buffer_enable_disabled and globalVariables.buffer_delay:

            if globalVariables.macro_loop_enable_disabled:
                mini_ftool_check = True
                toolControl.enable_disable_mini_ftool(button)

            if globalVariables.gt_buffer:
                gt_buffer_check = True
                globalVariables.gt_buffer = False

            windowsAPI.windows_api(globalVariables.buffs_hotbar)
            time.sleep(0.1)
            windowsAPI.windows_api(key)

            time.sleep(float(globalVariables.buffer_delay))

    windowsAPI.windows_api(globalVariables.previous_hotbar)

    if mini_ftool_check:
        toolControl.enable_disable_mini_ftool(button)

    if gt_buffer_check:
        globalVariables.gt_buffer = True

    mini_ftool_check = False
    gt_buffer_check = False


def gt_buffer():
    while True:
        if globalVariables.gt_buffer and globalVariables.gt_timer:
            windowsAPI.windows_api(globalVariables.gt_buffer_key)

            time.sleep(float(globalVariables.gt_timer))

        time.sleep(0.1)
