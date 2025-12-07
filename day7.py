F = open("input7")

def part1():
    totalSplits = 0
    beamIndices = set()
    for line in F:
        for i in range(len(line)):
            if line[i] == 'S':
                beamIndices.add(i)
            elif line[i] == '^':
                try: 
                    beamIndices.remove(i)
                    totalSplits += 1
                except:
                    None # type: ignore - do nothing

                beamIndices.add(i - 1)
                beamIndices.add(i + 1)
        
    print(totalSplits)

BLANK = "............................................................................................................................................."
def part2():
    beamIndices = [0 for _ in range(141)] # map of column to number of beams currently in it
    for line in F:
        line = line.strip()
        if line == BLANK:
            continue

        for col in range(len(line)):
            if not beamIndices[col]:
                beamIndices[col] = 0
            
            if line[col] == 'S':
                beamIndices[col] = 1
            elif line[col] == '^':
                num = beamIndices[col]
                beamIndices[col - 1] += num
                beamIndices[col + 1] += num
                beamIndices[col] = 0                
    
    total = 0
    for num in beamIndices:
        total += num
    
    print(total)

def main():
    part2()

main()