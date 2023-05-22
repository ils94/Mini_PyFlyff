import globalVariables
import windowsAPI


def alt_control_send_keys(key):
    if globalVariables.alt_control_on:
        windowsAPI.windows_api(key)
