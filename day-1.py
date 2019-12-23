# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

# thoughts
# input: list of numbers
# output: one number
# need to find out how to round down: import math and use math.floor
# divide mass by 3, math.floor results, subtract by 2
# sum up stuff, so need an empty variable set to 0

# input = 
[99711,
136867,
97107,
108257,
57509,
129721,
139889,
91988,
54465,
129229,
59122,
97391,
57509,
70687,
72733,
137687,
123889,
53484,
71869,
144816,
83856,
131570,
68905,
66648,
124392,
59964,
80553,
93881,
56253,
76282,
127377,
110425,
59914,
76294,
81888,
88986,
132544,
70423,
124018,
122121,
53231,
148042,
108810,
75092,
60185,
94065,
130221,
121319,
87502,
90029,
86186,
113956,
143744,
133441,
142914,
112218,
66629,
144965,
135476,
111537,
51709,
125198,
72098,
79625,
105068,
119597,
71611,
122186,
95752,
51967,
117725,
52696,
100411,
70222,
66330,
119579,
116075,
91228,
68982,
114698,
125333,
139219,
148789,
101768,
97593,
100820,
75959,
128572,
99469,
102120,
76462,
128313,
123442,
83860,
76163,
142707,
66275,
70837,
137203,
71123]

import math

def fuel_requirements(lst):
	total_fuel = 0

	for mass in lst:
		fuel = math.floor(mass/3) - 2
		total_fuel += fuel

	return total_fuel