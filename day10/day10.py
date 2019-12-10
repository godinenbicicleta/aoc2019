import math

data = """###..#########.#####.
.####.#####..####.#.#
.###.#.#.#####.##..##
##.####.#.###########
###...#.####.#.#.####
#.##..###.########...
#.#######.##.#######.
.#..#.#..###...####.#
#######.##.##.###..##
#.#......#....#.#.#..
######.###.#.#.##...#
####.#...#.#######.#.
.######.#####.#######
##.##.##.#####.##.#.#
###.#######..##.#....
###.##.##..##.#####.#
##.########.#.#.#####
.##....##..###.#...#.
#..#.####.######..###
..#.####.############
..##...###..#########"""

for line in data.split("\n"):
    print(line)

coords = [[j for j in i] for i in data.split("\n") ]

print(coords)

asteroids = []
for y,row in enumerate(coords):
    for x, k in enumerate(row):
        if k == "#":
            asteroids.append((x,y))

print(asteroids)

def gangle(a, b):
    x1, y1 = a
    x2, y2 = b
    if y2-y1 == 0 and x2>x1:
        return 0
    if y2-y1 == 0 and x2<x1:
        return 180
    if x2-x1 == 0 and y2> y1:
        return 90
    if x2-x1 == 0 and y1> y2: 
        return 270

    p = abs((y2-y1)/(x2-x1))

    if x2>x1 and y2 > y1:
        return math.degrees(math.atan(p))
    if x2>x1 and y2 < y1:
        return 360-math.degrees(math.atan(p))
    if x2 < x1 and y2 < y1:
        return 180 + math.degrees(math.atan(p))
    if x2 < x1 and y2 > y1:
        return 180-math.degrees(math.atan(p))



diccionario = {}
for current in asteroids:
    diccionario[current] = set()
    for asteroid in filter(lambda x: x!= current, asteroids):
        angle  = gangle(current, asteroid)
        diccionario[current].add(int(round(angle*1000)))

    diccionario[current] = len(diccionario[current])

print(max([k for k in diccionario.values()]))
