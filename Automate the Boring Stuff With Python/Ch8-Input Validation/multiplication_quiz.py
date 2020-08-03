# Multiplication Quiz

'''This program generates a multiplication quiz of 10 questions ranging from 0x0 to 9x9,
 giving the user only 3 tries and 8 seconds to answer.'''

import random
import time

score = 0

masterstarttime = time.time()
for x in range(10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    product = num1 * num2

    # Print question and take note of time before and after user answers
    print(f"What is {num1} x {num2}? ")
    starttime = time.time()
    user_answer = int(input())
    endtime = time.time()

    # Only accept answer three times
    for x in range(2):
        # Calculate how much time has elapsed
        timediff = endtime-starttime
        if user_answer == product:
            # Only accept if answered within 8 seconds
            if timediff <= 8:
                print('Correct!')
                score += 1
            else:
                print("Sorry, time ran out.")
            break
        else:
            user_answer = int(input("Wrong answer, Try again: "))
            continue

masterendtime = time.time()
time_elapsed = masterstarttime-masterendtime

print(
    f"Your score is {score}/10. You took {int(time_elapsed)} seconds.")
