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

# updating code
code[1] = 12
code[2] = 2

def intcode(code):
	print("in", code)
	for idx, num in enumerate(code):
		if idx % 4 == 0:

			if num == 99:
				break

			num1_idx = code[idx + 1]
			num2_idx = code[idx + 2]
			output_idx = code[idx + 3]

			if num == 1:
				output = code[num1_idx] + code[num2_idx]

			if num == 2:
				output = code[num1_idx] * code[num2_idx]

			code[output_idx] = output

	print("out", code)
	return code[0]
