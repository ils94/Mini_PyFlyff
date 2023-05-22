import time
import random
import windowsAPI
import globalVariables
from tkinter import messagebox


def macro_loop(check):
    while True:
        try:
            if globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:
                for key, timer in zip(globalVariables.macro_loop_keys, globalVariables.macro_loop_key_timers):
                    if globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:
                        windowsAPI.windows_api(key)

                        if check == 1:
                            time.sleep(random.uniform(0, float(timer)))
                        else:
                            time.sleep(float(timer))
        except Exception as e:
            messagebox.showerror("Error", "There is something wrong with the Mini Ftool Timers. "
                                          "Stop the loop and fix it."
                                          "\n\nError message: " + str(e))
            time.sleep(5)
            continue

        time.sleep(0.1)
