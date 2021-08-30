import time
import pyautogui


def locate_image(img, center=True, timeout=None, retries=None, **kwargs):
    locate = locate_box if not center else locate_center
    if timeout is None and retries is None:  # Single attempt
        return locate(img, **kwargs)
    elif timeout is None:  # Retries
        for i in range(retries + 1):
            loc = locate(img, **kwargs)
            if loc is not None:
                return loc
        return None
    # Timeout
    cur_time = round(time.time())
    while round(time.time()) < cur_time + timeout:
        loc = locate(img, **kwargs)
        if loc is not None:
            return loc


def locate_box(img, **kwargs):
    return pyautogui.locateOnScreen(img, **kwargs)


def locate_center(img, **kwargs):
    return pyautogui.locateCenterOnScreen(img, **kwargs)
