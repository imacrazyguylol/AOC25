f = open("input4")

def part1():
    grid = []
    for line in f:
        grid.append(line.strip())

    print(grid)

    count = 0
    for i in range(len(grid)):
        I = len(grid)
        for j in range(len(grid[i])):
            J = len(grid[i])
            adjRolls = 0
            if grid[i][j] == '.':
                continue
            
            if j + 1 < J:
                if grid[i][j + 1] == '@':
                    adjRolls += 1
            if i + 1 < I and j + 1 < J:
                if grid[i + 1][j + 1] == '@':
                    adjRolls += 1
            if i + 1 < I:
                if grid[i + 1][j] == '@':
                    adjRolls += 1
            if j - 1 >= 0 and i + 1 < I:
                if grid[i + 1][j - 1] == '@':
                    adjRolls += 1
            if j - 1 >= 0: 
                if grid[i][j - 1] == '@':
                    adjRolls += 1
            if i - 1 >= 0 and j - 1 >= 0:
                if grid[i - 1][j - 1] == '@':
                    adjRolls += 1
            if i - 1 >= 0:
                if grid[i - 1][j] == '@':
                    adjRolls += 1
            if i - 1 >= 0 and j + 1 < J: 
                if grid[i - 1][j + 1] == '@':
                    adjRolls += 1

            if adjRolls < 4:
                print(i, " ", j)
                count += 1

    print(count)

def part2():
    grid:list[str] = []
    for line in f:
        grid.append(line.strip())

    count = 0
    removed = 1
    while (removed > 0):
        removed = 0
        for i in range(len(grid)):
            I = len(grid)
            for j in range(len(grid[i])):
                J = len(grid[i])
                adjRolls = 0
                if grid[i][j] == '.':
                    continue
                
                if j + 1 < J:
                    if grid[i][j + 1] == '@':
                        adjRolls += 1
                if i + 1 < I and j + 1 < J:
                    if grid[i + 1][j + 1] == '@':
                        adjRolls += 1
                if i + 1 < I:
                    if grid[i + 1][j] == '@':
                        adjRolls += 1
                if j - 1 >= 0 and i + 1 < I:
                    if grid[i + 1][j - 1] == '@':
                        adjRolls += 1
                if j - 1 >= 0: 
                    if grid[i][j - 1] == '@':
                        adjRolls += 1
                if i - 1 >= 0 and j - 1 >= 0:
                    if grid[i - 1][j - 1] == '@':
                        adjRolls += 1
                if i - 1 >= 0:
                    if grid[i - 1][j] == '@':
                        adjRolls += 1
                if i - 1 >= 0 and j + 1 < J: 
                    if grid[i - 1][j + 1] == '@':
                        adjRolls += 1

                if adjRolls < 4:
                    # print(i, " ", j)
                    count += 1

                    grid[i] = grid[i][:j] + '.' + grid[i][j+1:]

                    removed += 1

    print(count)


def main():
    part2()

main()