# --- Day 2: 1202 Program Alarm --- PART 2

# Opcodes (like 1, 2, or 99) mark the beginning of an instruction.
# The values used immediately after an opcode, if any, are called the instruction's parameters.
# For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters.
# The instruction 99 contains only an opcode and has no parameters.

# The address of the current instruction is called the instruction pointer; it starts at 0.
# After an instruction finishes, the instruction pointer increases by the number of
# values in the instruction; until you add more instructions to the computer, this is ~
# always 4 (1 opcode + 3 parameters) for the add and multiply instructions.
# (The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)

# "With terminology out of the way, we're ready to proceed. To complete the gravity assist,
# you need to determine what pair of inputs produces the output 19690720."

# The inputs should still be provided to the program by replacing the values at addresses 1 and 2,
# just like before. In this program, the value placed in address 1 is called the noun, and the
# value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

# Once the program has halted, its output is available at address 0, also just like before.
# Each time you try a pair of inputs, make sure you first reset the computer's memory to the
# values in the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.

# Find the input noun and verb that cause the program to produce the output 19690720.
# What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)


def run(data):
    for start in range(0, len(data)-1, 4):
        end = start + 4
        opcode, idx_a, idx_b, output_idx = data[start:end]
        if opcode == 99:
            break
        elif opcode == 1:
            value_a, value_b = data[idx_a], data[idx_b]
            data[output_idx] = value_a+value_b
        elif opcode == 2:
            value_a, value_b = data[idx_a], data[idx_b]
            data[output_idx] = value_a*value_b
    return data[0]


# program = [1,1,1,4,99,5,6,0,99]
file = open('day2_my_input.txt')
_program = [int(i) for i in file.readline().split(',')]
file.close()

# settings for solution 2
noun, verb = 0, 0
for verb in range(100):
    for noun in range(100):
        program = _program.copy()
        program[2] = verb
        program[1] = noun
        try:
            if run(program) == 19690720:
                print(100 * noun+verb)
                break
        except IndexError:
            pass
