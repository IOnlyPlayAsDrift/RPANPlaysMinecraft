import praw
import pyautogui
import time

reddit = praw.Reddit(client_id='placeholder',
                     client_secret='placeholder',
                     user_agent='placeholder')

submissions = reddit.subreddit('pan_media')

for comment in submissions.stream.comments():
    print(30*'_')
    print()
    try:
        print(comment.author)
        comment = comment.body
        print(comment)
        if comment == "openinventory": pyautogui.press('e');
        if comment == "closeinventory": pyautogui.press('e');
        if comment == "moveforward": pyautogui.keyDown('w');
        if comment == "moveforwardcancel": pyautogui.press(['w', 'w', 'w']);
        if comment == "movebackward": pyautogui.keyDown('s');
        if comment == "movebackwardcancel": pyautogui.pyautogui.press(['s', 's', 's']);
        if comment == "moveleft": pyautogui.keyDown('a');
        if comment == "moveleftcancel": pyautogui.press(['a', 'a', 'a']);
        if comment == "moveright": pyautogui.keyDown('d');
        if comment == "moverightcancel": pyautogui.press(['d', 'd', 'd']);
        if comment == "slot1": pyautogui.press('1');
        if comment == "slot2": pyautogui.press('2');
        if comment == "slot3": pyautogui.press('3');
        if comment == "slot4": pyautogui.press('4');
        if comment == "slot5": pyautogui.press('5');
        if comment == "slot6": pyautogui.press('6');
        if comment == "slot7": pyautogui.press('7');
        if comment == "slot8": pyautogui.press('8');
        if comment == "slot9": pyautogui.press('9');
        if comment == "attackmob": pyautogui.mouseDown(duration=10.0);
        if comment == "attackcancel": pyautogui.click(button='primary');
        if comment == "mineveryshort": pyautogui.mouseDown(duration=1.0);
        if comment == "mineshort": pyautogui.mouseDown(duration=3.0);
        if comment == "minenormal": pyautogui.mouseDown(duration=5.0);
        if comment == "minelong": pyautogui.mouseDown(duration=7.0);
        if comment == "mineverylong": pyautogui.mouseDown(duration=9.0);
        if comment == "minecancel": pyautogui.click(button='primary');
        if comment == "lookleft": pyautogui.keyDown('num4'); time.sleep(1); pyautogui.keyUp('num4');
        if comment == "lookright": pyautogui.keyDown('num6'); time.sleep(1); pyautogui.keyUp('num6');
        if comment == "lookup": pyautogui.keyDown('num8'); time.sleep(1); pyautogui.keyUp('num8');
        if comment == "lookdown": pyautogui.keyDown('num2'); time.sleep(1); pyautogui.keyUp('num2');
        if comment == "resetcamera": pyautogui.keyDown('num5'); pyautogui.keyUp('num5');
        if comment == "jumpup": pyautogui.keyDown('space'); pyautogui.keyUp('space');
        if comment == "leftclick": pyautogui.click(button='primary');
        if comment == "rightclick": pyautogui.click(button='right');
        if comment == "eatfood": pyautogui.mouseDown(button='right', duration=5.0);
        if comment == "menuup": pyautogui.press('num8');
        if comment == "menudown": pyautogui.press('num2');
        if comment == "menuleft": pyautogui.press('num4');
        if comment == "menuright": pyautogui.press('num6');

    except:
        pass
