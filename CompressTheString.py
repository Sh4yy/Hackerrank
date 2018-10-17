from itertools import groupby

def print_compression(data):
	print(" ".join("({}, {})".format(x[0], x[1]) for x in data))

def compress_entirely(data):
	return map(lambda x: (len(list(x[1])), int(x[0])), 
		 	   groupby(str(data), lambda x: x))

def split(data):
	""" split based on any different value """
	result = []
	data = str(data)
	prev = None;
	last = 0

	for x in range(len(data)):
		if prev and prev == data[x]:
			pass
		elif prev:
			prev = data[x]
			result.append(data[last:x])
			last = x
		else:
			prev = data[x]

	result.append(data[last:])
	return result

def compress_continous(data):
	result = []
	for item in split(data):
		result.append(list(compress_entirely(item))[0])
	return result

print(compress_continous(input()))