import time
import random
import browserControl
import globalVariables


def mini_ftool(check):
    while True:
        try:
            if globalVariables.on:
                for key, timer in zip(globalVariables.mini_ftool_keys, globalVariables.mini_ftool_key_timers):
                    browserControl.firefox_window(key)

                    if check == 1:
                        time.sleep(random.uniform(0, float(timer)))
                    else:
                        time.sleep(float(timer))
        except Exception as e:
            print(e)
            time.sleep(1)
            continue

        time.sleep(1)
