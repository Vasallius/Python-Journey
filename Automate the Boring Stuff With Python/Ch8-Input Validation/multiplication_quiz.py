# Vasallius

'''This program generates a multiplication quiz of 10 questions ranging from 0x0 to 9x9,
 giving the user only 3 tries and 8 seconds to answer.'''

# Import necesarry modules
import random
import time


score = 0

# Create 10 questions
masterstarttime = time.time()
for x in range(10):
    # Initialize variables
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    product = num1 * num2

    # Print question and take note of time before and after user answers
    print(f"What is {num1} x {num2}? ")
    starttime = time.time()
    useranswer = int(input())
    endtime = time.time()

    # Only accept answer three times
    for x in range(2):
        # Calculated how much time has elapsed
        timediff = endtime-starttime
        if useranswer == product:
            # Check if 8 seconds have elapsed
            if timediff <= 8:
                print('Correct!')
                score += 1
            else:
                print("Time ran out.")
            break
        else:
            useranswer = int(input("Wrong answer, Try again: "))
            continue
masterendtime = time.time()
# Display total score
print(
    f"Your score is {score}/10. You took {int(masterendtime-masterstarttime)} seconds.")
