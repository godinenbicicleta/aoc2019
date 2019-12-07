from operator import add, mul
from itertools import permutations


#instructions = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]


ops = {
        1: add,
        2: mul,
        4: print
        }

index = 0

input_ixs = {0:0, 1:None, 2: None, 3: None, 4: None}

permut = permutations([0,1,2,3,4])
result_list = []
if __name__ == '__main__':
    for permu in permut:
        previous = 0
        nums3 = 0
        for ampli in (0,1,2,3,4):
            instructions = [3,8,1001,8,10,8,105,1,0,0,21,46,55,68,89,110,191,272,353,434,99999,3,9,1002,9,3,9,1001,9,3,9,102,4,9,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
            index = 0
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
                    if nums3 == 0:
                        instructions[instructions[index+1]] = permu[ampli]
                        nums3 = 1
                    else:
                        instructions[instructions[index+1]] = previous
                        nums3 = 0
                    index += 2
                    continue

                if opcode == 4:
                    mode = modes[-1]
                    if int(mode) == 0: # position
                        r = instructions[instructions[index+1]]
                    else:
                        r = instructions[index+1]
                    previous = r
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
        result_list.append([permu,r])

print(sorted(result_list, key = lambda x: x[1], reverse = True)[0])
