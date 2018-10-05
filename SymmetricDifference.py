
_ = int(input())
N = set([int(x) for x in input().split()])
_ = int(input())
M = set([int(x) for x in input().split()])

result = set()

intersection = N.intersection(M)
for x in N.difference(intersection):
    result.add(x)
for x in M.difference(intersection):
    result.add(x)x

for x in sorted(result):
	print(x)

