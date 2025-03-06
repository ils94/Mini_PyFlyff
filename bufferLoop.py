import time
import windowsAPI
import globalVariables
from tkinter import messagebox

buffer_countdown = None
buffer_default_countdown = None


def buffer_loop():
    global buffer_countdown
    global buffer_default_countdown

    try:

        if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on:

            globalVariables.buffer_is_going = True

            for key in globalVariables.buffer_hotkeys:

                if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on and globalVariables.buffer_is_going:

                    buffer_countdown = globalVariables.buffer_delay

                    if buffer_countdown:

                        buffer_countdown = float(globalVariables.buffer_delay)

                    else:

                        buffer_countdown = 3

                    windowsAPI.windows_api(globalVariables.buffs_hotbar)

                    time.sleep(0.5)

                    windowsAPI.windows_api(key)

                    while buffer_countdown:

                        if globalVariables.buffer_enable_disabled and globalVariables.buffer_is_on and globalVariables.buffer_is_going:

                            buffer_countdown = buffer_countdown - 1

                            time.sleep(1)

                        else:
                            break
                else:
                    globalVariables.buffer_is_going = False

                    windowsAPI.windows_api(globalVariables.previous_hotbar)

                    globalVariables.buffer_is_on = False

                    break

        globalVariables.buffer_is_going = False

        windowsAPI.windows_api(globalVariables.previous_hotbar)

        globalVariables.buffer_is_on = False

    except Exception as e:

        globalVariables.buffer_is_going = False

        windowsAPI.windows_api(globalVariables.previous_hotbar)

        globalVariables.buffer_is_on = False

        messagebox.showerror("Error", f"Something wrong with GT Buffer!\n\n{str(e)}")


def gt_buffer():
    while True:

        try:

            if not globalVariables.buffer_is_going:

                if globalVariables.gt_buffer:

                    countdown = globalVariables.gt_buffer_delay

                    if countdown:

                        countdown = float(globalVariables.gt_buffer_delay)

                    default_countdown = 45

                    windowsAPI.windows_api(globalVariables.gt_buffer_hotkey)

                    if globalVariables.gt_buffer_delay:

                        while countdown:

                            if globalVariables.gt_buffer_delay:

                                if globalVariables.gt_buffer:

                                    countdown = countdown - 1

                                    time.sleep(1)
                                else:
                                    break
                    else:
                        while default_countdown:

                            if globalVariables.gt_buffer:

                                default_countdown = default_countdown - 1

                                time.sleep(1)
                            else:
                                break
                else:
                    break

        except Exception as e:

            messagebox.showerror("Error", f"Something wrong with GT Buffer!\n\n{str(e)}")

            time.sleep(5)

            continue

        time.sleep(0.5)
