import fileinput

data = [line.strip().split(')') for line in fileinput.input()]

print(data)

#num of steps to com
total_steps = 0

links = {outsider: orbits  for orbits, outsider in data}

print(links)

def count_steps(outsider):
    if links[outsider] == 'COM': return 1
    else: 
        return 1 + count_steps(links[outsider])

for outsider in links:
    total_steps += count_steps(outsider)

print(total_steps)
