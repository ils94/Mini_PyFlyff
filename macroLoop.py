import time
import random
import windowsAPI
import globalVariables
from tkinter import messagebox


def macro_loop():
    while True:
        try:
            if globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:
                for key, timer in zip(globalVariables.macro_loop_hotkeys, globalVariables.macro_loop_hotkey_delay):
                    if globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:
                        windowsAPI.windows_api(key)

                        if globalVariables.macro_loop_random_delay == 1:
                            time.sleep(random.uniform(0, float(timer)))
                        else:
                            time.sleep(float(timer))

                    if not globalVariables.macro_loop_enable_disabled or not globalVariables.macro_loop_on:
                        break

            if not globalVariables.macro_loop_enable_disabled or not globalVariables.macro_loop_on:
                break

        except Exception as e:
            messagebox.showerror("Error", "There is something wrong with the Mini Ftool Timers. "
                                          "Stop the loop and fix it."
                                          "\n\nError message: " + str(e))
            time.sleep(5)
            continue

        time.sleep(0.5)
