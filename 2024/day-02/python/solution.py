import os

path = os.getcwd().replace("python", ".input")

# Parse input
ipt: list = [[eval(j) for j in i.replace('\n', '').split(' ')] for i in open(path, 'r').readlines()]

safe_updown: list = [i for i in ipt if len(set(['up' if v-i[j+1] > 0 else 'down' for j, v in enumerate(i[:-1])])) == 1]

safe_incr: list = [i for i in safe_updown if len(set(['ok' if (abs(v-i[j+1]) <=3 and abs(v-i[j+1]) > 0)  else 'ko' for j, v in enumerate(i[:-1])])) == 1]

print(len(safe_incr))

#tstsafe_incr: list = [[abs(v-i[j+1]) for j, v in enumerate(i[:-1])] for i in safe_updown]
#print(tstsafe_incr)
