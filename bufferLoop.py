import time
import windowsAPI
import globalVariables
import toolControl
from tkinter import messagebox

mini_ftool_check = False


def buffer_loop(button):
    global mini_ftool_check

    while True:
        try:
            if globalVariables.buffer_enable_disabled and globalVariables.buffer_timer:
                for key in globalVariables.buffer_keys:

                    if globalVariables.buffer_enable_disabled and globalVariables.buffer_timer:

                        if globalVariables.mini_ftool_enable_disabled:
                            mini_ftool_check = True
                            toolControl.enable_disable_mini_ftool(button)

                        windowsAPI.windows_api(globalVariables.buffs_hotbar)
                        time.sleep(0.1)
                        windowsAPI.windows_api(key)
                        time.sleep(3)

                windowsAPI.windows_api(globalVariables.previous_hotbar)

                if mini_ftool_check:
                    toolControl.enable_disable_mini_ftool(button)

                if globalVariables.buffer_timer and globalVariables.buffer_enable_disabled:
                    windowsAPI.windows_api(globalVariables.previous_hotbar)

                    time.sleep(float(globalVariables.buffer_timer))

        except Exception as e:
            messagebox.showerror("Error", str(e))
            time.sleep(5)
            continue

        time.sleep(0.1)


def gt_buffer():
    while True:
        windowsAPI.windows_api("1")

        time.sleep(10)
