# Vasallius

# Import necessary modules
import time
import pyperclip

start_button = input(
    'Press Enter to start stopwatch. Press Ctrl + C to quit.\n')

# Only accept "Enter" to start the stop watch
while True:
    if not len(start_button) < 1:
        start_button = input('Press enter to start stopwatch.\n')
    else:
        break

# Set variables
start_time = time.time()
before_time = start_time
lap_number = 0
while True:
    # Track lap times
    try:
        input()
        now_time = time.time()
        lap_time = round(now_time - before_time, 2)
        before_time = now_time
        lap_number += 1
        total_time = round(now_time - start_time, 2)
        lap_result = (
            f"Lap #{lap_number} {str(total_time).rjust(6)} ({lap_time})")
        print(lap_result, end='')
        pyperclip.copy(lap_result)
    except:  # Handle the Ctrl + C error to keep from displaying
        KeyboardInterrupt
        print('\n Stopwatch Exiting Now..')
        break
