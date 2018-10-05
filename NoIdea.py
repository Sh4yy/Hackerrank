
input()
N = [int(x) for x in input().split()]
A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])

happiness = 0

for n in N:
    if n in A:
        happiness += 1
    if n in B:
        happiness -= 1

print(happiness)