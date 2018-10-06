def solve(s):
	result = ""
	was_space = True
	for char in s:
		if was_space:
			result += str(char).upper()
		else:
			result += str(char)
		if char == ' ':
			was_space = True
		if char != ' ':
			was_space = False

	return result

print(solve("132 456 Wq  m e"))