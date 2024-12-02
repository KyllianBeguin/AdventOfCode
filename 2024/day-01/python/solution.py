import os

path = os.getcwd().replace("python", ".input")

# Parse input
ipt: list = [i.replace('\n', '').split('   ') for i in open(path, 'r').readlines()]
l1: list = [eval(i[0]) for i in ipt]
l2: list = [eval(i[1]) for i in ipt]

# PART ONE =====
# Order lists
l1.sort()
l2.sort()

dist:list = [abs(v - l2[i]) for i, v in enumerate(l1)]

# PART TWO =====

# Detect numbers from l1 in l2
det: list = [i * l2.count(i) for i in l1 if i in l2]

print(sum(det))
