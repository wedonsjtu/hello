import itertools

n = 8
L = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8]))

'''
def is_valid(px, py, qx, qy):
    return px != qx and py != qy and abs(qx - px) != abs(qy - py)


sum = 0

for p in L:
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if not is_valid(i, p[i], j, p[j]):
                break
            j += 1
        if j < n:
            break
        i += 1
    if i == n:
        sum += 1
        print(p)
print(sum)
'''


def valid(ax, ay, bx, by):
    return ax != bx and ay != by and abs(ax - bx) != abs(ay - by)


s = 0
list1 = ['0', '0', '0', '0', '0', '0', '0', '0']
list2 = []
for i in range(8):
    list2.append(list1.copy())


def renew():
    global list2
    for iv in list2:
        for ii in range(8):
            iv[ii] = '0'


for p in L:
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if not valid(i, p[i], j, p[j]):
                break
            j += 1

        if j < n:
            break
        i += 1

    if i == n:
        #        s += 1
        #        print(p)
        print(p)
        for nnn in range(8):
            list2[nnn][p[nnn] - 1] = '1'
        for iii in list2:
            print(' '.join(iii))
        print('\n')
        renew()


nn = 0
for p in L:
    try:
        for i in range(n):
            for j in range(i+1, n):
                assert valid(i, p[i], j, p[j])
        nn += 1
    except AssertionError:
        pass

print(nn)
