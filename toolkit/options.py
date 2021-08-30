import pyautogui

SAFE_SPOT = (0, pyautogui.size().height - 10)


def set_safe(x, y):
    global SAFE_SPOT
    SAFE_SPOT = (x, y)
