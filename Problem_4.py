x = 1000
result = 0

for a in range(x):
    for b in range(x):
        if (str(a*b)) == (str(a*b)[::-1]):
            if a*b > result:
                result = a*b

print(result)

