import math
F = open("input8")

def part1():
    closestNeighbors:dict[tuple[int,int,int], tuple[tuple[int,int,int], float]]  = {} # map junctiion to a tuple of (closest neighbor, distance)
    for line in F:
        tokens = line.split(',')

        x, y, z = int(tokens[0]), int(tokens[1]), int(tokens[2])

        for junction in closestNeighbors:
            i, j, k = junction[0], junction[1], junction[2]
            dist = math.sqrt(
                (x - i) ** 2 +
                (y - j) ** 2 +
                (z - k) ** 2
            )

            if dist < closestNeighbors[junction][1]:
                closestNeighbors[junction] = (x,y,z), dist

    circuits:list[set[tuple[int, int, int]]] = []

    for junction in closestNeighbors:
        

def main():
    part1()

main()