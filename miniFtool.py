import time
import random
import browserControl
import globalVariables
from tkinter import messagebox


def mini_ftool(check):
    while True:
        try:
            if globalVariables.mini_ftool_on and globalVariables.mini_ftool_enable_disabled:
                for key, timer in zip(globalVariables.mini_ftool_keys, globalVariables.mini_ftool_key_timers):
                    browserControl.mini_ftool_send_keys(key)

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
