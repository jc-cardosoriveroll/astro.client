
# encoding: utf-8
# coder:    Ishaq Khan
# version:  1.1

import os
import sys
import argparse
import psutil
import time
import keyboard
import subprocess
import re
import pygetwindow
import unidecode
import requests

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

if not os.path.exists('steps.txt'):
    print('`steps.txt` not exists in the root directory of the executable. Program exited.')
    sys.exit()

print('*' * 22)
print('** JCAutomator v1.1 **')
print('*' * 22)

print('\nProcess started...')
print('Parsing steps file')

steps_file_op = open('steps.txt', encoding='utf-8')
steps = steps_file_op.read().strip().split('\n')
steps = [eve for eve in steps if eve.startswith('FOCUS') or eve.startswith('WAIT') or eve.startswith('SENDKEY') or eve.startswith('TERMINATE') or eve.startswith('TYPETEXT') or eve.startswith('GETURL')]
print(f'{len(steps)} step{"" if len(steps) == 1 else "s"} found')

norm_key = {'LShift': 'shift', 'RShift': 'right shift', 'LCtrl': 'ctrl', 'RCtrl': 'right ctrl', 'LAlt': 'alt', 'RAlt': 'right alt', 'Menu': 'menu', 'Windows': 'right windows', 'Print Screen': 'print screen', 'Insert': 'insert', 'Del': 'delete', 'Left': 'left', 'Right': 'right', 'Up': 'up', 'Down': 'down', 'Num Lock': 'num lock', 'Tab': 'tab', 'F1': 'f1', 'F2': 'f2', 'F3': 'f3', 'F4': 'f4', 'F5': 'f5', 'F6': 'f6', 'F7': 'f7', 'F8': 'f8', 'F9': 'f9', 'F10': 'f10', 'F11': 'f11', 'F12': 'f12', 'PageUp': 'page up', 'PageDn': 'page down', 'Home': 'home', 'Caps Lock': 'caps lock', 'Enter': 'enter', 'Space': 'space', 'Backspace': 'backspace', 'Plus' : '+'}

for step in steps:
    print(step)

    try:
        step_type, step_value = step.split(' ', 1)

        if step_type == 'FOCUS':
            exe_path = step_value.strip('"\'')

            if os.path.basename(exe_path) in (i.name() for i in psutil.process_iter()):
                tl_com = f'tasklist /fi "imagename eq {os.path.basename(exe_path)}" /fo list /v'
                tl_com_out = subprocess.check_output(tl_com).decode('utf-8')
                win_title = re.search('(?<=Window Title: ).*(?=\r)', tl_com_out)
                win_title = tl_com_out[win_title.start():win_title.end()]

                app_win_exists = pygetwindow.getWindowsWithTitle(win_title)
                app_win_exists[0].restore()
                app_win_exists[0].activate()

            else:
                os.startfile(exe_path)

        elif step_type == 'WAIT':
            time.sleep(float(step_value))

        elif step_type == 'SENDKEY':
            prep_hk = unidecode.unidecode(step_value.replace(' ', '')).split('+')
            prep_hk = [norm_key.get(eve, eve) for eve in prep_hk]
            keyboard.send('+'.join(prep_hk))

        elif step_type == 'TERMINATE':
            exe_path = step_value.strip('"\'')
            exe_name = os.path.basename(exe_path)

            for proc in psutil.process_iter():
                if proc.name() == exe_name:
                    proc.kill()

        elif step_type == 'TYPETEXT':
            k_delay = re.search('\d+(\.\d+)?$', step_value)
            if k_delay:
                k_delay = float(step_value[k_delay.start():k_delay.end()])
                text_to_type = step_value.removesuffix(str(k_delay))
                text_to_type = text_to_type.strip('" ')
            else:
                text_to_type = step_value.strip('"')
                k_delay = 0

            keyboard.write(text_to_type, delay=k_delay, exact=True)

        elif step_type == 'GETURL':
            requests.get(step_value.strip('"\''), headers={'User-Agent': 'Mozilla/5.0'})

    except:
        print('Command execution failed.')

print('Process completed successfully!')
