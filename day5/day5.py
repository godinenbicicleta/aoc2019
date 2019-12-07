from operator import add, mul


instructions = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,65,73,225,1101,37,7,225,1101,42,58,225,1102,62,44,224,101,-2728,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1,69,126,224,101,-92,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,41,84,225,1001,22,92,224,101,-150,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,80,65,225,1101,32,13,224,101,-45,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1101,21,18,225,1102,5,51,225,2,17,14,224,1001,224,-2701,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,101,68,95,224,101,-148,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,12,22,225,102,58,173,224,1001,224,-696,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1002,121,62,224,1001,224,-1302,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,374,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,389,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,419,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,434,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1008,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,659,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226]
#instructions = [3,3,1107,-1,8,3,4,3,99]
input_num = 5

ops = {
        1: add,
        2: mul,
        4: print
        }

index = 0


if __name__ == '__main__':

    while instructions[index] != 99:
        instruction = str(instructions[index])
        opcode = int(instruction[-2:])
        modes = instruction[:-2].zfill(3)


        values = {}
        if opcode == 1 or opcode == 2:
            for num,mode in enumerate(modes[::-1]):
                if int(mode) == 0: # position
                    values[num] = instructions[instructions[index+num+1]]
                else:
                    values[num] = instructions[index+num+1]
            res = ops[opcode](values[0],values[1])
            instructions[instructions[index+3]] = res
            index += 4
            continue

        if opcode == 3:
            instructions[instructions[index+1]] = input_num
            index += 2
            continue

        if opcode == 4:
            mode = modes[-1]
            if int(mode) == 0: # position
                print(instructions[instructions[index+1]])
            else:
                print(instructions[index+1])
            index += 2
            continue

        if opcode == 5:
            modes = instruction[:-2].zfill(2)
            for num,mode in enumerate(modes[::-1]):
                if int(mode) == 0: # position
                    values[num] = instructions[instructions[index+num+1]]
                else:
                    values[num] = instructions[index+num+1]
            if values[0] != 0:
                index  = values[1]
            else:
                index += 3
            continue

        if opcode == 6:
            modes = instruction[:-2].zfill(2)
            for num,mode in enumerate(modes[::-1]):
                if int(mode) == 0: # position
                    values[num] = instructions[instructions[index+num+1]]
                else:
                    values[num] = instructions[index+num+1]
            if values[0] == 0:
                index  = values[1]
            else:
                index += 3

            continue

        if opcode == 7:
            for num,mode in enumerate(modes[::-1]):
                if int(mode) == 0: # position
                    values[num] = instructions[instructions[index+num+1]]
                else:
                    values[num] = instructions[index+num+1]
            if values[0] < values[1]:
                instructions[instructions[index+3]] = 1
            else:
                instructions[instructions[index+3]] = 0

            index+=4
            continue

        if opcode == 8:
            for num,mode in enumerate(modes[::-1]):
                if int(mode) == 0: # position
                    values[num] = instructions[instructions[index+num+1]]
                else:
                    values[num] = instructions[index+num+1]
            if values[0] == values[1]:
                instructions[instructions[index+3]] = 1
            else:
                instructions[instructions[index+3]] = 0

            index += 4
            continue
        break
