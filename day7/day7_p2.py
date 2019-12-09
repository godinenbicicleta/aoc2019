from operator import add, mul
from itertools import permutations


# instructions = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]


ops = {1: add, 2: mul, 4: print}

instructions = [ 3,8,1001,8,10,8,105,1,0,0,21,46,55,68,89,110,191,272,353,434,99999,3,9,1002,9,3,9,1001,9,3,9,102,4,9,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]

class Amplifier:
    def __init__(self, instructions, phase, name):
        self.instructions = instructions[:]
        self.phase = phase
        self.name = name
        self.nums3 = 0
        self.index = 0
        self.halted = False

    def start(self, second):
        while self.instructions[self.index] != 99:
            instruction = str(self.instructions[self.index])
            opcode = int(instruction[-2:])
            modes = instruction[:-2].zfill(3)
#            print('opcode: ', opcode, ' ', 'self.index', self.index )

            values = {}
            if opcode == 1 or opcode == 2:
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                res = ops[opcode](values[0], values[1])
                self.instructions[self.instructions[self.index + 3]] = res
                self.index += 4
                continue

            if opcode == 3:
                if self.nums3 == 0:
                    self.instructions[self.instructions[self.index + 1]] = self.phase
                    self.nums3 = 1
                else:
                    self.instructions[self.instructions[self.index + 1]] = second
                self.index += 2
                continue

            if opcode == 4:
                mode = modes[-1]
                if int(mode) == 0:  # position
                    r = self.instructions[self.instructions[self.index + 1]]
                else:
                    r = self.instructions[self.index + 1]
                self.output = r
                self.index += 2
                break

            if opcode == 5:
                modes = instruction[:-2].zfill(2)
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                if values[0] != 0:
                    self.index = values[1]
                else:
                    self.index += 3
                continue

            if opcode == 6:
                modes = instruction[:-2].zfill(2)
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                if values[0] == 0:
                    self.index = values[1]
                else:
                    self.index += 3

                continue

            if opcode == 7:
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                if values[0] < values[1]:
                    self.instructions[self.instructions[self.index + 3]] = 1
                else:
                    self.instructions[self.instructions[self.index + 3]] = 0

                self.index += 4
                continue

            if opcode == 8:
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                if values[0] == values[1]:
                    self.instructions[self.instructions[self.index + 3]] = 1
                else:
                    self.instructions[self.instructions[self.index + 3]] = 0

                self.index += 4
                continue

        if self.instructions[self.index] == 99:
            self.halted = True

    def __repr__(self):
        return f"Amplifier({self.name}, {self.phase}) = {self.instructions}"




def play(permut):
    amplis = []
    for name, phase in enumerate(permut):
        amplis.append(Amplifier(instructions, phase, name))
    amplis[0].start(0)
    while True:
        amplis[1].start(amplis[0].output)
        amplis[2].start(amplis[1].output)
        amplis[3].start(amplis[2].output)
        amplis[4].start(amplis[3].output)
        amplis[0].start(amplis[4].output)
        if all([a.halted for a in amplis]):
            
            return amplis[4].output


final = []
for permut in permutations([5,6,7,8,9]):
    final.append([permut, play(list(permut))])

print(sorted(final, key = lambda x: x[1])[-1])
