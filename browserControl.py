import win32gui
import win32api
import win32con
import time
import virtualKeys
import globalVariables


def alt_control_send_keys(key):
    if globalVariables.alt_control_on:
        window = win32gui.FindWindow("MozillaWindowClass", None)
        win32api.SendMessage(window, win32con.WM_KEYDOWN, virtualKeys.vk_code.get(key), 0)
        time.sleep(0.1)
        win32api.SendMessage(window, win32con.WM_KEYUP, virtualKeys.vk_code.get(key), 0)


def mini_ftool_send_keys(key):
    window = win32gui.FindWindow("MozillaWindowClass", None)
    win32api.SendMessage(window, win32con.WM_KEYDOWN, virtualKeys.vk_code.get(key), 0)
    time.sleep(0.1)
    win32api.SendMessage(window, win32con.WM_KEYUP, virtualKeys.vk_code.get(key), 0)
