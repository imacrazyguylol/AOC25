f = open("input5")

def part1():
    arr:list[list[int]] = []

    count = 0
    countIDs = False
    for line in f:
        line = line.strip()
        if not countIDs:
            if not line:
                countIDs = True
                continue
            
            tokens = line.split('-')
            arr.append([int(tokens[0]), int(tokens[1])])
            # print(arr)
        else:
            for idRange in arr:
                if int(line) >= idRange[0] and int(line) <= idRange[1]:
                    print(line, ": ", idRange)
                    count += 1
                    break

    print(count)
            
def part2():
    ranges:list[list[str]] = [] # unparsed
    count = 0
    for line in f:
        line = line.strip()
        if not line:
            break

        minID, maxID = line.split('-')
        minID = int(minID) - 1 # exclusive
        maxID = int(maxID)

        maxVal = maxID # the amount to subtract from maxID - minID is maxVal - minID
        minVal = minID
        for minR, maxR in ranges:
            minR = int(minR)
            maxR = int(maxR)

            if maxR > minID:
                if maxR < maxVal: # r is fully contained inside ID
                    maxVal -= maxR
                else: # r overlaps only max of ID
                    maxID = minR
                
                

        count += (maxID - minID) - (maxVal - minVal)

        ranges.append( line.split('-') )
    
    print(count)

# returns amount 
def checkOverlap(ranges:list[tuple[int, int]], idRange:tuple[int, int]):
    overlapMax, overlapMin = idRange 
    # overlapMin = the min of the overlap on the upper part of the range
    # overlapMax = the max of the overlap on the lower part of the range

    for r in ranges:
        if idRange[0] < r[1] and idRange[1] > r[1]:
            if overlapMax < r[1]:
                overlapMax = r[1]
        if idRange[1] > r[0] and idRange[0] < r[0]:
            if overlapMin > r[0]:
                overlapMin = r[0]
    
    if overlapMin < overlapMax:
        return (overlapMax - overlapMin)
    else:
        return (idRange[1] - overlapMin) + (overlapMax - idRange[0])

def main():
    part2()

main()