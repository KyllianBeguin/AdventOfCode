import os

path = os.getcwd().replace("python", ".input")

# Parse input
ipt = [i.replace('\n', '').split('   ') for i in open(path, 'r').readlines()]
l1: list = [eval(i[0]) for i in ipt]
l2: list = [eval(i[1]) for i in ipt]

# Order lists
l1.sort()
l2.sort()

dist = [abs(v - l2[i]) for i, v in enumerate(l1)]

print(sum(dist))
