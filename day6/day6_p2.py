import fileinput

data = [line.strip().split(')') for line in fileinput.input()]

print(data)

#num of steps to SAM
total_steps = 0

links = {outsider: orbits  for orbits, outsider in data}
reverse = {orbits: outsider for orbits, outsider in data}


print(links)

#find COM for you and san (point in common)


def get_route(outsider):
    if links[outsider] == 'COM': return [outsider]
    else: 
        return [outsider] + get_route(links[outsider])

my_route = get_route('YOU')
print(my_route)
san_route = get_route('SAN')
print(san_route)

my_set = set(my_route)
san_set = set(san_route)


def count_steps(outsider, goal = 'COM'):
    if links[outsider] == goal: return 1
    else: 
        return 1 + count_steps(links[outsider], goal)

inter = my_set.intersection(san_set)
print(inter)

minimum =  1000000000000
for pos in inter:
    print(pos)
    print('steps YOU')
    print(count_steps('YOU', pos))
    if count_steps('YOU', pos) + count_steps('SAN', pos) < minimum:
        minimum = count_steps('YOU', pos) + count_steps('SAN', pos) 

print(minimum)
