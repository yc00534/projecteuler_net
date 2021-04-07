a = 1
b = 1

for aa in range(2, 1000000):
    a, b = b, b + a
    if len(str(a)) == 1000:
        print(aa, " > ", a)
        break
