import globalVariables
import windowsAPI


def alt_control_send_keys(key):
    if globalVariables.alt_controller_on:
        windowsAPI.windows_api(key)
