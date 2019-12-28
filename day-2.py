import random

# PART 1
# input: list of integers
# output integer at position 0

# opcode: 1 (adds), 2 (multiplies), 99 (stop)

# program: 0, 1, 2, 3, 4...
# opcode, idx of num1, idx of num2, output idx...(repeat)
# get value at specified idx position and do opcode on it

# before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

# input:
code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]

# thoughts
# create function
# first thing is to 
# (1) replace value at idx 1 = 12
# (2) replace value at position 2 = 2 

# loop through list, enumerate? get value AND idx
# define opcodes
# if idx % 4 == 0: should get idx 0, 4, 8, etc.

# fail fast: if value is 99, break loop

# else:
# get value of idx + 1 and idx + 2
# get value from list indicated at idx + 1 and idx + 2
# perform opcode on values grabbed from list
# insert value at idx + 3

# outside loop
# return list[0]

# PART 2
# instructions = 1, 2, 3, 4 
# 1 = opcode (1, 2, 99)
# 2, 3, 4, = parameters (99 does not have parameters)

# which pair of inputs output 19690720
# oh! a position in memory is also called an address (idx?)
# noun = address 1; verb = address 2
# each two inputs are between 0 - 99 inclusive 
# need to reset/use clean inputs w/out manipulation 

# OH!! input = like.. addresses at idx 1 and 2 (noun, verb)
# inputs between 0 - 99 inclusive 
# which pair will produce output of 19690720

# hmm.. some sort of binary search algorithm? 
# noun 0 - 49, verb between 50 - 99
# if output is too big, bring verb down into 0 - 49
# if output too small, bring noun to 50 - 99
# reset the list to original 
# have an empty list storing what we've seen so we don't have repeats

# after find noun and verb
# what is 100 * noun + verb??



def intcode(code):
	# updating code
	# seen numbers
	working_code = code
	seen = []
	noun = working_code[1] 
	verb = working_code[2]
	
	print('noun', noun)
	print('verb', verb)
	final_output = working_code[0]

	while final_output < 19690720:
		# resetting the input to original code
		working_code = code
		if noun not in seen:
			noun = random.randint(0, 49)
			seen.append(noun)
			working_code[1] = noun

		if verb not in seen:
			verb = random.randint(50, 99)
			seen.append(verb)
			working_code[2] = verb

		print('seen', seen)

		print("in", working_code)
		for idx, num in enumerate(working_code):
			if idx % 4 == 0:
				num1_idx = working_code[idx + 1]
				num2_idx = working_code[idx + 2]
				output_idx = working_code[idx + 3]

				if num == 99:
					break

				if num == 1:
					output = working_code[num1_idx] + working_code[num2_idx]

				if num == 2:
					output = working_code[num1_idx] * working_code[num2_idx]

				working_code[output_idx] = output
				print('output_idx', output_idx)
				print('output', output)

	print("out", working_code)
	return working_code[0]
