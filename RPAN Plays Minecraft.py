import praw
import pyautogui
import time
from idlecolors import *

reddit = praw.Reddit(client_id='placeholder',
                     client_secret='placeholder',
                     user_agent='placeholder')

subreddit = reddit.subreddit('pan_media')

for comment in subreddit.stream.comments():
    if comment.parent() == "placeholder":
        print(30*'_')
        print()
        try:
            print(comment.author)
            comment = comment.body
            printc( randcol(comment))
            if comment == "openinv": pyautogui.press('e');
            if comment == "closeinv": pyautogui.press('e');
            if comment == "invopen": pyautogui.press('e');
            if comment == "invclose": pyautogui.press('e');
            if comment == "forward": pyautogui.keyDown('w');
            if comment == "forwardstop": pyautogui.press(['w', 'w', 'w']);
            if comment == "fwd": pyautogui.keyDown('w');
            if comment == "fwdstop": pyautogui.press(['w', 'w', 'w']);
            if comment == "backward": pyautogui.keyDown('s');
            if comment == "backwardstop": pyautogui.press(['s', 's', 's']);
            if comment == "bkwd": pyautogui.keyDown('s');
            if comment == "bkwdstop": pyautogui.press(['s', 's', 's']);
            if comment == "left": pyautogui.keyDown('a');
            if comment == "leftstop": pyautogui.press(['a', 'a', 'a']);
            if comment == "right": pyautogui.keyDown('d');
            if comment == "rightstop": pyautogui.press(['d', 'd', 'd']);
            if comment == "1": pyautogui.press('1');
            if comment == "2": pyautogui.press('2');
            if comment == "3": pyautogui.press('3');
            if comment == "4": pyautogui.press('4');
            if comment == "5": pyautogui.press('5');
            if comment == "6": pyautogui.press('6');
            if comment == "7": pyautogui.press('7');
            if comment == "8": pyautogui.press('8');
            if comment == "9": pyautogui.press('9');
            if comment == "attack": pyautogui.click(clicks=10);
            if comment == "attackstop": pyautogui.click(button='primary');
            if comment == "atk": pyautogui.click(clicks=10);
            if comment == "atkstop": pyautogui.click(button='primary');
            if comment == "mine": pyautogui.mouseDown(duration=5.0);
            if comment == "minestop": pyautogui.click(button='primary');
            if comment == "cleft": pyautogui.keyDown('num4'); time.sleep(0.5); pyautogui.keyUp('num4');
            if comment == "cright": pyautogui.keyDown('num6'); time.sleep(0.5); pyautogui.keyUp('num6');
            if comment == "cup": pyautogui.keyDown('num8'); time.sleep(0.5); pyautogui.keyUp('num8');
            if comment == "cdown": pyautogui.keyDown('num2'); time.sleep(0.5); pyautogui.keyUp('num2');
            if comment == "creset": pyautogui.keyDown('x'); pyautogui.keyUp('x');
            if comment == "camleft": pyautogui.keyDown('num4'); time.sleep(0.5); pyautogui.keyUp('num4');
            if comment == "camright": pyautogui.keyDown('num6'); time.sleep(0.5); pyautogui.keyUp('num6');
            if comment == "camup": pyautogui.keyDown('num8'); time.sleep(0.5); pyautogui.keyUp('num8');
            if comment == "camdown": pyautogui.keyDown('num2'); time.sleep(0.5); pyautogui.keyUp('num2');
            if comment == "camreset": pyautogui.keyDown('x'); pyautogui.keyUp('x');
            if comment == "jump": pyautogui.keyDown('space'); pyautogui.keyUp('space');
            if comment == "lc": pyautogui.click(button='primary');
            if comment == "rc": pyautogui.click(button='right');
            if comment == "eat": pyautogui.mouseDown(button='right');
            if comment == "eatstop": pyautogui.click(button='right');
            if comment == "menuup": pyautogui.press('num8');
            if comment == "menudown": pyautogui.press('num2');
            if comment == "menuleft": pyautogui.press('num4');
            if comment == "menuright": pyautogui.press('num6');
            if comment == "select": pyautogui.press('enter');
            if comment == "place": pyautogui.press('enter');

        except:
            pass
