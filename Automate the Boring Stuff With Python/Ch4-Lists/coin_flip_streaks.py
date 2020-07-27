# Coin Flip Streaks

import random

number_of_streaks = 0  # Counter for streaks
master_list = []

for experiment_number in range(10000):  # Perform experiment 10,000 times

    for i in range(100):
        if random.randint(0, 1) == 0:
            master_list.append('H')
        else:
            master_list.append('T')
    print(master_list)  # print list for visualization
    for x in range(94):  # Used 94, to prevent IndexError
        if master_list[x:x+6] == ['H'] * 6 or master_list[x:x+6] == ['T'] * 6:
            number_of_streaks += 1
            print('STREAK FOUND!')
            break
    master_list = []  # Without this, master_list keeps on growing as new data is appended to it

print('')
print('Experimentation complete.')
print(f'Chance of streak: {(number_of_streaks / 10000 * 100)}%')
