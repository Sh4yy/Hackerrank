
def get_three_common(name):
	
	data = {}
	for char in name:
		data[char] = data.get(char, 0) - 1

	sorted_tuples = sorted(zip(data.keys(),
	 						   data.values()),
					 	   key=lambda x: (x[1], x[0]))

	for value, count in sorted_tuples[0:3]:
		print("{} {}".format(value, abs(count)))

get_three_common("aabbbccde")