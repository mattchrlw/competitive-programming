from copy import deepcopy
from pprint import pprint

f = open("day11.txt", "r")
data = [i.replace("\n", "") for i in f.readlines()]

def day1():
    grid = []
    for i in data:
        grid.append([j for j in i])
    new_grid = deepcopy(grid)

    count = 0
    while True:
        count += 1
        grid = deepcopy(new_grid)
        # pprint(grid)
        for idx, i in enumerate(grid):
            for jdx, j in enumerate(i):
                adjacent = 0
                if idx-1 >= 0 and grid[idx-1][jdx] == '#':
                    adjacent += 1
                if jdx-1 >= 0 and grid[idx][jdx-1] == '#':
                    adjacent += 1
                if idx+1 < len(grid) and grid[idx+1][jdx] == '#':
                    adjacent += 1
                if jdx+1 < len(i) and grid[idx][jdx+1] == '#':
                    adjacent += 1
                if idx-1 >= 0 and jdx-1 >= 0 and grid[idx-1][jdx-1] == '#':
                    adjacent += 1
                if idx-1 >= 0 and jdx+1 < len(i) and grid[idx-1][jdx+1] == '#':
                    adjacent += 1
                if idx+1 < len(grid) and jdx-1 >= 0 and grid[idx+1][jdx-1] == '#':
                    adjacent += 1
                if idx+1 < len(grid) and jdx+1 < len(i) and grid[idx+1][jdx+1] == '#':
                    adjacent += 1
                if grid[idx][jdx] == '#' and adjacent >= 4:
                    new_grid[idx][jdx] = 'L'
                if grid[idx][jdx] == 'L' and adjacent == 0:
                    new_grid[idx][jdx] = '#'
        if grid == new_grid and count >= 1:
            # print(count)
            break
    return sum([len([j for j in i if j == '#']) for i in new_grid])

def day2():
    grid = []
    for i in data:
        grid.append([j for j in i])
    new_grid = deepcopy(grid)

    count = 0
    while True:
        count += 1
        grid = deepcopy(new_grid)
        # pprint(grid)
        for idx, i in enumerate(grid):
            for jdx, j in enumerate(i):
                adjacent = 0
                for m in range(1, max(len(grid), len(i))):
                    if idx-m < 0 or (idx-m >= 0 and grid[idx-m][jdx] == 'L'):
                        break
                    if idx-m >= 0 and grid[idx-m][jdx] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if jdx-m < 0 or (jdx-m >= 0 and grid[idx][jdx-m] == 'L'):
                        break
                    if jdx-m >= 0 and grid[idx][jdx-m] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if idx+m >= len(grid) or (idx+m < len(grid) and grid[idx+m][jdx] == 'L'):
                        break
                    if idx+m < len(grid) and grid[idx+m][jdx] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if jdx+m >= len(i) or (jdx+m < len(i) and grid[idx][jdx+m] == 'L'):
                        break
                    if jdx+m < len(i) and grid[idx][jdx+m] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if idx-m < 0 or jdx-m < 0 or (idx-m >= 0 and jdx-m >= 0 and grid[idx-m][jdx-m] == 'L'):
                        break
                    if idx-m >= 0 and jdx-m >= 0 and grid[idx-m][jdx-m] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if idx-m < 0 or jdx+m >= len(i) or (idx-m >= 0 and jdx+m < len(i) and grid[idx-m][jdx+m] == 'L'):
                        break
                    if idx-m >= 0 and jdx+m < len(i) and grid[idx-m][jdx+m] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if idx+m >= len(grid) or jdx-m < 0 or (idx+m < len(grid) and jdx-m >= 0 and grid[idx+m][jdx-m] == 'L'):
                        break
                    if idx+m < len(grid) and jdx-m >= 0 and grid[idx+m][jdx-m] == '#':
                        adjacent += 1
                        break
                for m in range(1, max(len(grid), len(i))):
                    if idx+m >= len(grid) or jdx+m >= len(i) or (idx+m < len(grid) and jdx+m < len(i) and grid[idx+m][jdx+m] == 'L'):
                        break
                    if idx+m < len(grid) and jdx+m < len(i) and grid[idx+m][jdx+m] == '#':
                        adjacent += 1
                        break
                if grid[idx][jdx] == '#' and adjacent >= 5:
                    new_grid[idx][jdx] = 'L'
                if grid[idx][jdx] == 'L' and adjacent == 0:
                    new_grid[idx][jdx] = '#'
        if grid == new_grid and count >= 1:
            # print(count)
            break
        # print(grid)
    return sum([len([j for j in i if j == '#']) for i in new_grid])
    # print(new_grid[0])
print("Part 1:", day1())
print("Part 2:", day2())