#!/usr/bin/python
import time
import sys
import argparse

# Help String
description_string = "Tomaterminal is a terminal program based on the Pomodoro (Italian for Tomato) method of working. In the Pomodoro method, you take a timer ((frequently tomato shaped) historically used in kitchens) and you set a 25 minute timer for work. After 25 mintues are completed, you set a 5 minute timer for break. Tomaterminal emulates this exact behavior, alerting you after 25 minutes have elapsed, then after your 5 minute break has elapsed."

parser = argparse.ArgumentParser(description=description_string)
parser.add_argument('-t','--task_time', type=int, help='Task Interval (minutes)',required=False)
parser.add_argument('-b','--break_time', type=int, help='Break Interval (minutes)',required=False)
parser.add_argument('-m','--task_name', type=str, help='Task Name (in quotations. ex: "Hello World")',required=False)
args = parser.parse_args()

# Time Definitions
seconds_minute = 60
minutes_hour = 60
hours_day = 24

# Task Definitions
task_time = 25
break_time = 5
task_name = "current task"

# Override task/break time if command line arguments passed
if args.task_time is not None:
    task_time = args.task_time
if args.break_time is not None:
    break_time = args.break_time
if args.task_name is not None:
    task_name = args.task_name

# UI Definitions
progress_bar_length = 40

def alert():
    print ('\a')

def progress(count, total, suffix=''):
    filled_len = int(round(progress_bar_length * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (progress_bar_length - filled_len)
    sys.stdout.write("\r[%s] %s%s %s" % (bar, percents, '%', suffix)),
    sys.stdout.flush()

# Initial Entry into Program; Clear Screen
while True:

    # Task Loop
    progress(0,task_time,'Working: %smin to go on %s' % (task_time, task_name))
    for i in range(0, task_time):
        ellapsedTime = task_time - i
        if ellapsedTime < 10:
            ellapsedTime = str(ellapsedTime).zfill(2)
        time.sleep(seconds_minute)
        progress(i,task_time,'Working: %smin to go on %s' % (ellapsedTime, task_name))

    alert()

    # Break Loop
    progress(0,task_time,'Break: %smin left' % break_time)
    for i in range(0, break_time):
        breakTimeEllapsed = break_time - i;
        breakTimeEllapsed = str(ellapsedTime).zfill(2)
        time.sleep(seconds_minute)
        progress(i,break_time,'Break: %smin left' % breakTimeEllapsed)

    alert()
