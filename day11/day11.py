from operator import add, mul
from itertools import permutations


# instructions = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]


ops = {1: add, 2: mul, 4: print}

instructions = [
3,8,1005,8,327,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,28,1006,0,42,2,1104,11,10,1006,0,61,2,1005,19,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,65,1006,0,4,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,89,1,1108,10,10,1,1103,11,10,1,109,18,10,1006,0,82,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,126,2,109,7,10,1,104,3,10,1006,0,64,2,1109,20,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,163,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,185,2,1109,12,10,2,103,16,10,1,107,11,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,219,1,1005,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,245,2,1002,8,10,1,2,9,10,1006,0,27,1006,0,37,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,281,1006,0,21,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,306,101,1,9,9,1007,9,1075,10,1005,10,15,99,109,649,104,0,104,1,21102,1,847069852568,1,21101,344,0,0,1105,1,448,21101,0,386979963688,1,21101,355,0,0,1105,1,448,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,46346031251,1,1,21101,0,402,0,1105,1,448,21102,1,29195594775,1,21101,0,413,0,1105,1,448,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,868498428772,1,21101,0,436,0,1106,0,448,21102,718170641172,1,1,21102,1,447,0,1105,1,448,99,109,2,21202,-1,1,1,21102,40,1,2,21102,1,479,3,21102,1,469,0,1105,1,512,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,474,475,490,4,0,1001,474,1,474,108,4,474,10,1006,10,506,1101,0,0,474,109,-2,2106,0,0,0,109,4,2102,1,-1,511,1207,-3,0,10,1006,10,529,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21101,0,1,3,21101,548,0,0,1106,0,553,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,576,2207,-4,-2,10,1006,10,576,21202,-4,1,-4,1106,0,644,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,595,0,1105,1,553,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,614,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,636,22102,1,-1,1,21102,1,636,0,106,0,511,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0
        ]

#2461214151
#instructions = instructions + [0 for _ in range(2000)]
#print(instructions)

mode_dict = {0:0, 2: 1}

class Amplifier:
    def __init__(self, instructions, phase, name):
        self.instructions = instructions[:]
        self.phase = phase
        self.name = name
        self.nums3 = 0
        self.index = 0
        self.relative_base = 0
        self.halted = False

    def start(self, second = None):
        self.num_outputs = 0
        self.outs = []
        while self.instructions[self.index] != 99:
            if self.num_outputs>1:
                break
            instruction = str(self.instructions[self.index])
            opcode = int(instruction[-2:])
            modes = instruction[:-2].zfill(3)
            print(
            'opcode: ', opcode, ' ', 'self.index', self.index, 'relbase:',
            self.relative_base, 'modes: ', modes)

            values = {}
            if opcode == 1 or opcode == 2:
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    elif int(mode) == 1:
                        values[num] = self.instructions[self.index + num + 1]
                    else:
                        values[num] =self.instructions[
                                self.instructions[
                                    self.index + num + 1 ]+ self.relative_base
                                    
                            ]
                res = ops[opcode](values[0], values[1])
                self.instructions[self.instructions[self.index + 3] +
                        self.relative_base * mode_dict[int(modes[0])]] = res
                self.index += 4
                continue

            if opcode == 3:
                mode = modes[-1]
                if int(mode) == 0:  # position
                    self.instructions[self.instructions[self.index + 1]] = self.phase
                else:
                    self.instructions[self.instructions[self.index + 1] +
                            self.relative_base] = self.phase
                self.index += 2
                continue

            if opcode == 4:
                mode = modes[-1]
                if int(mode) == 0:  # position
                    r = self.instructions[self.instructions[self.index + 1]]
                elif int(mode) == 1:
                    r = self.instructions[self.index + 1]
                else:
                    r = self.instructions[self.instructions[self.index + 1] +
                        self.relative_base]
                self.output = r
                self.outs.append(r)
                print(r)
                self.num_outputs += 1
                self.index += 2

            if opcode == 5:
                modes = instruction[:-2].zfill(2)
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    elif int(mode) == 2:
                        values[num] =(
                        self.instructions[self.instructions[self.index + num +
                            1 ]+ self.relative_base])

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
                    elif int(mode) == 2:
                        values[num] =(
                        self.instructions[self.instructions[self.index + num +
                            1] + self.relative_base])
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
                    elif int(mode) == 2:
                        values[num] =(
                        self.instructions[self.instructions[self.index + num +
                            1] + self.relative_base])
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                if values[0] < values[1] :
                    self.instructions[self.instructions[self.index + 3] +
                            self.relative_base * mode_dict[int(modes[0])]] = 1
                else:
                    self.instructions[self.instructions[self.index + 3] + 
                        self.relative_base * mode_dict[int(modes[0])]
                            ] = 0

                self.index += 4
                continue

            if opcode == 8:
                for num, mode in enumerate(modes[::-1]):
                    if int(mode) == 0:  # position
                        values[num] = self.instructions[self.instructions[self.index + num + 1]]
                    elif int(mode) == 2:
                        values[num] =(
                        self.instructions[self.instructions[self.index + num +
                            1 ]+ self.relative_base])
                    else:
                        values[num] = self.instructions[self.index + num + 1]
                if values[0] == values[1]:

                    self.instructions[self.instructions[self.index + 3] +
                            self.relative_base * mode_dict[int(modes[0])]] = 1


                else:
                    self.instructions[self.instructions[self.index + 3] + 
                        self.relative_base * mode_dict[int(modes[0])]
                            ] = 0

                self.index += 4
                continue

            if opcode == 9:
                """
                Opcode 9 adjusts the relative base by the value of its only
                parameter. The relative base increases (or decreases, if the
                value is negative) by the value of the parameter"""
                mode = modes[-1]
                #print("mode9: ", mode)
                if int(mode) == 0:
                    r = self.instructions[self.instructions[self.index + 1]]
                elif int(mode) == 1:
                    r = self.instructions[self.index + 1 ]
                else:
                    r = self.instructions[self.instructions[self.index + 1] +
                        self.relative_base]
                self.relative_base +=  r
                self.index += 2



    def __repr__(self):
        return f"Amplifier({self.name}, {self.phase}) = {self.instructions}"




amp = Amplifier(instructions, 0, 'test')

pos = (0,0,"^")
def turn(num, pos):
    if actual == "^" and num == 0:
        return (pos[0]-1,pos[1],"<")
    if actual == "^" and num == 1:
        return (pos[0]+1, pos[1],">")
    if actual == "v" and num == 0:
        return (pos[0]+1,pos[1],">")
    if actual == "v" and num == 1:
        return (pos[0]-1,pos[1],"<")
    if actual == ">" and num == 0:
        return (pos[0], pos[1]+1, "^")
    if actual == ">" and num == 1:
        return (pos[0], pos[1]-1, "v")
    if actual == "<" and num == 1:
        return (pos[0], pos[1]+1, "^")
    if actual == "<" and num == 0:
        return (pos[0], pos[1]-1, "v")



colors = {(0,0):'black'}
inputs ={0:'black', 1:'white'} 
positions = set()
while amp.instructions[amp.index] != 99:
    amp.start()
    if pos in colors:
        colors[pos] = inputs[amp.outs[0]]
    else:
        colors[pos] = inputs
    pos = turn(amp.outs[1], pos)
    positions.add((pos[0], pos[1]))
    if pos in colors:
        self.phase = inputs[colors[pos]]
    else:
        self.phase = inputs[colors[pos]]
