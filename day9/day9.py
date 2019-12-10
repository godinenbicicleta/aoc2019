from operator import add, mul
from itertools import permutations


# instructions = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]


ops = {1: add, 2: mul, 4: print}

instructions = [
        1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,30,1016,1101,37,0,1005,1101,362,0,1023,1101,0,20,1014,1101,39,0,1013,1102,34,1,1007,1101,682,0,1027,1102,664,1,1025,1102,1,655,1028,1101,0,26,1002,1102,1,38,1015,1101,669,0,1024,1101,0,28,1017,1102,1,21,1000,1101,0,27,1012,1102,1,29,1008,1102,1,23,1019,1101,0,24,1011,1101,685,0,1026,1102,646,1,1029,1102,1,369,1022,1101,0,31,1003,1102,1,36,1001,1101,0,0,1020,1102,1,35,1009,1101,32,0,1010,1101,0,1,1021,1102,33,1,1004,1101,22,0,1006,1102,1,25,1018,109,14,1205,6,197,1001,64,1,64,1105,1,199,4,187,1002,64,2,64,109,-4,21107,40,39,9,1005,1019,219,1001,64,1,64,1105,1,221,4,205,1002,64,2,64,109,9,1206,1,239,4,227,1001,64,1,64,1106,0,239,1002,64,2,64,109,-9,2101,0,-8,63,1008,63,26,63,1005,63,261,4,245,1106,0,265,1001,64,1,64,1002,64,2,64,109,-6,2108,37,1,63,1005,63,287,4,271,1001,64,1,64,1105,1,287,1002,64,2,64,109,15,21108,41,44,-2,1005,1017,307,1001,64,1,64,1106,0,309,4,293,1002,64,2,64,109,-16,1207,1,34,63,1005,63,327,4,315,1105,1,331,1001,64,1,64,1002,64,2,64,109,8,1208,-9,29,63,1005,63,347,1106,0,353,4,337,1001,64,1,64,1002,64,2,64,109,4,2105,1,8,1001,64,1,64,1105,1,371,4,359,1002,64,2,64,109,-22,1201,9,0,63,1008,63,27,63,1005,63,391,1106,0,397,4,377,1001,64,1,64,1002,64,2,64,109,18,21107,42,43,5,1005,1016,415,4,403,1106,0,419,1001,64,1,64,1002,64,2,64,109,-8,1201,2,0,63,1008,63,37,63,1005,63,441,4,425,1105,1,445,1001,64,1,64,1002,64,2,64,109,27,1205,-9,463,4,451,1001,64,1,64,1106,0,463,1002,64,2,64,109,-1,1206,-8,475,1105,1,481,4,469,1001,64,1,64,1002,64,2,64,109,-6,21101,43,0,-8,1008,1015,43,63,1005,63,507,4,487,1001,64,1,64,1106,0,507,1002,64,2,64,109,-15,2101,0,-3,63,1008,63,35,63,1005,63,531,1001,64,1,64,1106,0,533,4,513,1002,64,2,64,109,-2,2102,1,-6,63,1008,63,18,63,1005,63,553,1105,1,559,4,539,1001,64,1,64,1002,64,2,64,109,7,21102,44,1,3,1008,1016,44,63,1005,63,581,4,565,1105,1,585,1001,64,1,64,1002,64,2,64,109,-11,1202,7,1,63,1008,63,34,63,1005,63,609,1001,64,1,64,1105,1,611,4,591,1002,64,2,64,109,6,1202,1,1,63,1008,63,35,63,1005,63,637,4,617,1001,64,1,64,1106,0,637,1002,64,2,64,109,16,2106,0,4,4,643,1001,64,1,64,1106,0,655,1002,64,2,64,109,-1,2105,1,1,4,661,1106,0,673,1001,64,1,64,1002,64,2,64,109,5,2106,0,-1,1105,1,691,4,679,1001,64,1,64,1002,64,2,64,109,-24,1208,-2,26,63,1005,63,709,4,697,1105,1,713,1001,64,1,64,1002,64,2,64,109,-10,2102,1,6,63,1008,63,21,63,1005,63,735,4,719,1105,1,739,1001,64,1,64,1002,64,2,64,109,25,21108,45,45,-9,1005,1010,757,4,745,1106,0,761,1001,64,1,64,1002,64,2,64,109,-12,1207,-7,20,63,1005,63,777,1106,0,783,4,767,1001,64,1,64,1002,64,2,64,109,-13,2108,22,6,63,1005,63,799,1106,0,805,4,789,1001,64,1,64,1002,64,2,64,109,17,21102,46,1,0,1008,1011,45,63,1005,63,825,1105,1,831,4,811,1001,64,1,64,1002,64,2,64,109,-6,2107,21,1,63,1005,63,849,4,837,1105,1,853,1001,64,1,64,1002,64,2,64,109,-3,2107,27,0,63,1005,63,873,1001,64,1,64,1105,1,875,4,859,1002,64,2,64,109,12,21101,47,0,0,1008,1014,48,63,1005,63,899,1001,64,1,64,1105,1,901,4,881,4,64,99,21102,27,1,1,21101,0,915,0,1105,1,922,21201,1,42931,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,21202,1,1,-1,21201,-2,-3,1,21102,1,957,0,1106,0,922,22201,1,-1,-2,1106,0,968,22101,0,-2,-2,109,-3,2106,0,0
        ]

#2461214151
instructions = instructions + [0 for _ in range(2000)]
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
        while self.instructions[self.index] != 99:
            instruction = str(self.instructions[self.index])
            opcode = int(instruction[-2:])
            modes = instruction[:-2].zfill(3)
 #           print(
 #           'opcode: ', opcode, ' ', 'self.index', self.index, 'relbase:',
 #           self.relative_base, 'modes: ', modes)

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
                print(r)
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




amp = Amplifier(instructions, 1, 'test')
amp.start()
amp = Amplifier(instructions, 2, 'prod')
amp.start()
