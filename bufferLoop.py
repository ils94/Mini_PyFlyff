import time
import windowsAPI
import globalVariables
import macroLoop
import miscs

macro_loop_on_check = None

macro_loop_enable_disable_check = None

gt_buffer_check = False

buffer_countdown = None
buffer_default_countdown = None


def buffer_loop(button1, button2, button3):
    global macro_loop_on_check
    global gt_buffer_check
    global macro_loop_enable_disable_check
    global buffer_countdown
    global buffer_default_countdown

    if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

        macro_loop_on_check = globalVariables.macro_loop_on

        macro_loop_enable_disable_check = globalVariables.macro_loop_enable_disabled

        gt_buffer_check = globalVariables.gt_buffer

        for key in globalVariables.buffer_keys:

            buffer_countdown = globalVariables.buffer_delay

            if buffer_countdown:
                buffer_countdown = float(globalVariables.buffer_delay)

            buffer_default_countdown = 3

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

                if buffer_countdown:
                    while buffer_countdown:
                        if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on and globalVariables.buffer_delay:
                            buffer_countdown = buffer_countdown - 1
                            time.sleep(1)
                else:
                    while buffer_default_countdown:
                        if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:
                            buffer_default_countdown = buffer_default_countdown - 1
                            time.sleep(1)

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
                miscs.multithreading(gt_buffer)

            miscs.multithreading(lambda: macroLoop.macro_loop())


def gt_buffer():
    while globalVariables.gt_buffer:

        countdown = float(globalVariables.gt_buffer_delay)

        default_countdown = 45

        windowsAPI.windows_api(globalVariables.gt_buffer_hotbar)
        time.sleep(1)
        windowsAPI.windows_api(globalVariables.gt_buffer_key)

        if globalVariables.gt_buffer_delay and globalVariables.gt_buffer:

            while countdown:
                if globalVariables.gt_buffer and globalVariables.gt_buffer_delay:
                    countdown = countdown - 1
                    time.sleep(1)
        else:
            while default_countdown:
                if globalVariables.gt_buffer:
                    default_countdown = default_countdown - 1
                    time.sleep(1)

    time.sleep(0.5)
