import time
import random
import windowsAPI
import globalVariables
from tkinter import messagebox


def macro_loop():
    while True:

        try:

            if not globalVariables.buffer_is_going:

                if globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled:

                    for key, timer in zip(globalVariables.macro_loop_hotkeys, globalVariables.macro_loop_hotkey_delay):

                        if globalVariables.macro_loop_on and globalVariables.macro_loop_enable_disabled and not globalVariables.buffer_is_going:

                            windowsAPI.windows_api(key)

                            if globalVariables.macro_loop_random_delay == 1:

                                time.sleep(random.uniform(0, float(timer)))

                            else:

                                time.sleep(float(timer))
                        else:
                            break
                else:
                    break

        except Exception as e:

            messagebox.showerror("Error", f"Something wrong with Macro Loop!\n\n{str(e)}")

            time.sleep(5)

            continue

        time.sleep(0.5)
