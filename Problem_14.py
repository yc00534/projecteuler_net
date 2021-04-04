import sys
sys.setrecursionlimit(3000)

zahl = 0
count = 0
res = 0


def pos(n):
    start(n / 2)


def neg(n):
    start(3 * n + 1)


def start(n):
    global count
    count = count + 1
    if n >= 2:
        if n % 2 == 0:
            pos(n)
        else:
            neg(n)


for x in range(0, 1000000):
    start(x)
    if count > res:
        res = count
        zahl = x
    count = 0

print("Rs ", res, " -> Zahl = ", zahl)
