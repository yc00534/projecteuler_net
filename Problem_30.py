tmp = 0
result = 0

for x in range(1000, 200000):
    strX = str(x)
    for y in range(len(strX)):
        tmp += int(strX[y])**5
    if(tmp==x):
        result += tmp
    tmp = 0
print(result)
