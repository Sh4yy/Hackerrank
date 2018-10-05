from collections import OrderedDict

words = []
for _ in range(int(input())):
    words.append(input())
count = OrderedDict()

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(len(count.values()))
print(' '.join([str(x) for x in count.values()]))

