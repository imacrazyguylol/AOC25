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
    ranges:list[tuple[int, int]] = [] # unparsed
    count = 0
    for line in f:
        line = line.strip()
        if not line:
            break

        minID, maxID = line.split('-')
        minID = int(minID)
        maxID = int(maxID)
        
        overlapMin, overlapMax = checkOverlap(ranges, minID, maxID)

        if overlapMin < overlapMax:
            amt = (maxID - minID) - (overlapMax - overlapMin)
            print("= ", amt, sep="")
            count += amt
        else:
            amt = (maxID - minID) - ((maxID - overlapMin) + (overlapMax - minID))
            print("= ", amt, sep="")
            count += amt

        ranges.append( (minID, maxID) )
    
    print("\n", count, sep="")

# returns amount 
def checkOverlap(ranges:list[tuple[int, int]], minID, maxID):
    print(minID, "-", maxID, sep="")

    overlapMax, overlapMin = minID, maxID
    # the -1 would only adjust overlapMax in the subtraction if it remains unchanged, otherwise we dont need to
    # overlapMin = the min of the overlap on the upper part of the range
    # overlapMax = the max of the overlap on the lower part of the range
    for r in ranges:
        if (r[0] > minID and r[1] < maxID):
            print("recurse lower: ", r, sep="")
            olMinLower, olMaxLower = checkOverlap(ranges, minID, r[0])
            print("recurse upper: ", r, sep="")
            olMinUpper, olMaxUpper = checkOverlap(ranges, r[1], maxID)

            minID = olMaxLower
            maxID = olMinUpper

            print("new range: ", minID, "-", maxID, sep="")
            print("overlapMin: ", olMinLower, "; overlapMax: ", olMaxUpper, sep="")

            return olMinLower, olMaxUpper # we already check all the ranges in the recursive, no need to do it again

        if minID < r[1] and maxID > r[1]:
            if overlapMax < r[1]:
                overlapMax = r[1]
        if maxID > r[0] and minID < r[0]:
            if overlapMin > r[0]:
                overlapMin = r[0]
        if (minID >= r[0] and maxID <= r[1]):
            return overlapMax, overlapMin

    return overlapMin, overlapMax

def main():
    part2()

main()