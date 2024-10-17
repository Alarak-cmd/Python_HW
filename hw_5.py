""" import math

def alfa(m):
    al = math.acos(int(m[0])/math.sqrt(int(m[0]) ** 2 + int(m[1]) ** 2))
    return al

x = input().split()
y = input().split()
z = input().split()
corns = [alfa(x), alfa(y), alfa(z)]
if min(corns) == alfa(x):
    print(x)
elif min (corns) == alfa(y):
    print(y)
else:
    print """

""" def func(n):
    counter = 0
    for i in range(2, n):
        if n % i == 0:
            counter += 1
    if counter == 0:
        res = True
    else:
        res = False
    return res

n = int(input())
for i in range(2, n):
    if str(i) == str(i)[::-1]:
        if func(i):
            print(i, end=' ') """
