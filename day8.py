import math
F = open("input8")

def part1():
    junctions = []
    dists = {}
    for line in F:
        tokens = line.split(',')

        x, y, z = int(tokens[0]), int(tokens[1]), int(tokens[2])

        for i, j, k in junctions:
            dist = math.sqrt( 
                (x - i) ** 2 +
                (y - j) ** 2 +
                (z - k) ** 2
            )

            if dist in dists:
                print("holy shit")
            dists[dist] = ((x,y,z), (i,j,k))

        junctions.append((x, y, z))
    
    sortedDists = sorted(dists.keys())
    circuits:list[set[tuple[int, int, int]]] = []

    for i in range(len(sortedDists)):
        a, b = dists[sortedDists[i]]
        connected = False
        for c in circuits:
            if a in c:
                c.add(b)
                connected = True
                break
            elif b in c:
                c.add(a)
                connected = True
                break
        
        if not connected:
            s = set()
            s.add((a, b))
            circuits.append(s)

    sortedCircuits = sorted(circuits, key=(lambda x : len(x)))
    print( len(sortedCircuits[0]) * len(sortedCircuits[1]) * len(sortedCircuits[2]))
    print(circuits)

def main():
    part1()

main()