# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

number_of_items_in_list = len(grid[0])
number_of_lists = len(grid)

print('Here is the resulting character grid. \n')

for i in range(number_of_items_in_list):
    for x in range(number_of_lists):
        print(grid[x][i], end='')
    print('')
