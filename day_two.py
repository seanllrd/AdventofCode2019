def part_one(intcode):
    for i in range(0, len(intcode), 4):
        try:
            opcode = intcode[i]
            if opcode == 1:
                first_number = intcode[intcode[i + 1]]
                second_number = intcode[intcode[i + 2]]
                intcode[intcode[i + 3]] = first_number + second_number
            if opcode == 2:
                first_number = intcode[intcode[i + 1]]
                second_number = intcode[intcode[i + 2]]
                intcode[intcode[i + 3]] = first_number * second_number
            if opcode == 99:
                break
        except IndexError:
            return "Error"
    return intcode


def part_two(intcode):
    noun = 0
    verb = 0
    while noun < 100:
        while verb < 100:
            test_intcode = intcode[:]
            test_intcode[1] = noun
            test_intcode[2] = verb
            test_intcode = part_one(test_intcode)
            if type(test_intcode) == list:
                if test_intcode[0] == 19690720:
                    return [noun, verb, 100 * noun + verb]
            verb += 1
        noun += 1
        verb = 0


print(part_two(
    [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 9, 19, 23, 2, 13, 23, 27, 1, 6, 27, 31, 2, 6, 31,
     35, 2, 13, 35, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 9, 47, 51, 1, 51, 13, 55, 1, 55, 13, 59, 2, 59, 13, 63, 1, 63,
     6, 67, 2, 6, 67, 71, 1, 5, 71, 75, 2, 6, 75, 79, 1, 5, 79, 83, 2, 83, 6, 87, 1, 5, 87, 91, 1, 6, 91, 95, 2, 95, 6,
     99, 1, 5, 99, 103, 1, 6, 103, 107, 1, 107, 2, 111, 1, 111, 5, 0, 99, 2, 14, 0, 0]))
