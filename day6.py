import re


F = open('input6')

def part1():
    problems:list[list[int]] = []
    ops:list[str] = []

    grandTotal = 0
    for line in F:
        line = line.strip()
        row:list[int] = []
        isOpsRow = False
        for token in re.split(r'\s+', line):
            if token == '*' or token == '+':
                isOpsRow = True
                ops.append(token)
            else:
                row.append(int(token))
        
        if not isOpsRow:
            problems.append(row)
    
    for c in range(len(problems[0])):
        isMult = ops[c] == '*' # true -> multiply, false -> add
        total = int(isMult)
        for r in range(len(problems)):
            if isMult:
                total *= problems[r][c]
            else:
                total += problems[r][c]

        grandTotal += total

    print(grandTotal)

def part2():
    problems:list[list[str]] = []
    ops:list[str] = []

    opsString = F.readline()[:-1] # edited input to put ops on top :3
    ops = re.split(r'\s+', opsString.strip())
    opsAndLen = re.split(r'\s(\*|\+)', opsString)
    opsAndLen.pop(0)
    # list of each operator followed by the whitespace/columns. The whitespace length + the operator = number of columns
    print(opsAndLen)
    i = 0
    for line in F:
        line = line[1:-1]
        problems.append([])        
        colSize = 0
        for op in opsAndLen:
            if op == '*' or op == '+':
                colSize += 1
                continue

            colSize += len(op)
            problems[i].append(line[:colSize].replace(' ', '0')) # add exactly the width to the column, with leading and trailing 0s
            line = line[(colSize + 1):] # skip the next whitespace and trim off the front of the string
            colSize = 0 # reset colsize for next iter

        i += 1

    grandTotal = 0
    # print(ops)
    print(problems)
    for c in range(len(problems[0])):
        isMult = ops[c] == '*' # true -> multiply, false -> add
        total = int(isMult)

        digits = []
        for r in range(len(problems)):
            digits.append([int(x) for x in problems[r][c]])
            
        # print(digits)
        for col in range(len(digits[0])):
            num = 0
            for row in range(len(digits)):
                if digits[row][col] != 0:
                    num *= 10

                num += digits[row][col]
            
            if isMult:
                total *= num
            else:
                total += num
        
        grandTotal += total
            

    # print(digitColArr)
    print(grandTotal)

def main():
    part2()

main()
