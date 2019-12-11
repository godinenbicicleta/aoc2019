import math

data = """#....#.....#...#.#.....#.#..#....#
#..#..##...#......#.....#..###.#.#
#......#.#.#.....##....#.#.....#..
..#.#...#.......#.##..#...........
.##..#...##......##.#.#...........
.....#.#..##...#..##.....#...#.##.
....#.##.##.#....###.#........####
..#....#..####........##.........#
..#...#......#.#..#..#.#.##......#
.............#.#....##.......#...#
.#.#..##.#.#.#.#.......#.....#....
.....##.###..#.....#.#..###.....##
.....#...#.#.#......#.#....##.....
##.#.....#...#....#...#..#....#.#.
..#.............###.#.##....#.#...
..##.#.........#.##.####.........#
##.#...###....#..#...###..##..#..#
.........#.#.....#........#.......
#.......#..#.#.#..##.....#.#.....#
..#....#....#.#.##......#..#.###..
......##.##.##...#...##.#...###...
.#.....#...#........#....#.###....
.#.#.#..#............#..........#.
..##.....#....#....##..#.#.......#
..##.....#.#......................
.#..#...#....#.#.....#.........#..
........#.............#.#.........
#...#.#......#.##....#...#.#.#...#
.#.....#.#.....#.....#.#.##......#
..##....#.....#.....#....#.##..#..
#..###.#.#....#......#...#........
..#......#..#....##...#.#.#...#..#
.#.##.#.#.....#..#..#........##...
....#...##.##.##......#..#..##...."""

coords = [[j for j in i] for i in data.split("\n") ]


asteroids = []
for y,row in enumerate(coords):
    for x, k in enumerate(row):
        if k == "#":
            asteroids.append((x,y))


def gangle(a, b):
    x1, y1 = a
    x2, y2 = b
    if y2-y1 == 0 and x2>x1:
        return 0
    if y2-y1 == 0 and x2<x1:
        return 180
    if x2-x1 == 0 and y2 < y1:
        return 90
    if x2-x1 == 0 and y1 < y2: 
        return 270

    p = abs((y2-y1)/(x2-x1))

    if x2>x1 and y2 < y1:
        return math.degrees(math.atan(p))
    if x2>x1 and y2 > y1:
        return 360-math.degrees(math.atan(p))
    if x2 < x1 and y2 > y1:
        return 180 + math.degrees(math.atan(p))
    if x2 < x1 and y2 < y1:
        return 180-math.degrees(math.atan(p))


def distancia(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2-x1)**2+ (y2-y1)**2)

diccionario = {}
total_angles = set()
for current in asteroids:
    diccionario[current] = {}
    for asteroid in filter(lambda x: x!= current, asteroids):
        angle  = gangle(current, asteroid)
        angle = int(round(angle*1000))
        total_angles.add(angle)
        if angle not in diccionario[current]:
            diccionario[current][angle]  = [asteroid]
        else:
            diccionario[current][angle].append(asteroid)

        for angle in diccionario[current]:
            diccionario[current][angle] = sorted(diccionario[current][angle],
                    key = lambda x: distancia(x,current), reverse = True)


best_len = 0
for pos in diccionario:
    if len(diccionario[pos]) > best_len:
        best_len = len(diccionario[pos])
        best_pos = pos


def add(angle):
    if angle >= 0 and angle <= 90*1000:
        return angle + 1000000
    return angle

best_angles = [(a, add(a)) for a in diccionario[best_pos]]


best_angles = sorted(best_angles, key = lambda x:x[1], reverse = True)

pops = 0

print(best_pos)
while True:
    for num,(angle, _) in enumerate(best_angles):
        try:
            poped = diccionario[best_pos][angle].pop()
            pops += 1
            print("pos: ", pops,"poped: ",poped, "angle: ",angle)

        except:
            continue
    if all([len(v) == 0 for v in diccionario[best_pos].values()]):
        break

