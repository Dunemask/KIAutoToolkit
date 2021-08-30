import time
import pyautogui

from toolkit.image_tool import locate_image
from toolkit.options import SAFE_SPOT


def mouse_move(x, y=None, travel=0):
    if y is None and type(x) is tuple or type(x) is list:
        y = x[1]
        x = x[0]
    pyautogui.moveTo(x, y, travel)


def click(**kwargs):
    """
    :param kwargs: x (point/int), y (int), travel (float)
    :return:
    """
    mouse_move(**kwargs)
    pyautogui.click()


def click_delay(delay, **kwargs):
    """
    :param delay: how long to hold the mouse down
    :param kwargs: x (point/int), y (int), travel (float)
    :return:
    """
    pyautogui.moveTo(**kwargs)
    pyautogui.mouseDown()
    time.sleep(delay)
    pyautogui.mouseUp()


def rel_move(x, y, travel=0):
    pyautogui.moveRel(x, y, travel)


def click_image(img, delay=0, travel=0, no_fail=False, **kwargs):
    loc = locate_image(img, True, **kwargs)
    if loc is not None:
        click_delay(loc, delay=delay, travel=travel)
    elif not no_fail:
        raise Exception(f"Failed to find image {img}")
    return loc


def hover_image(img, no_fail=False, travel=0, **kwargs):
    loc = locate_image(img, True, **kwargs)
    if loc is not None:
        pyautogui.moveTo(loc, duration=travel)
    elif not no_fail:
        raise Exception(f"Failed to find image {img}")
    return loc


def safe_move(spot=SAFE_SPOT, travel=0):
    mouse_move(spot, travel=travel)
