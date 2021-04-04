tmp = 2**1000
result = 0
str_tmp = str(tmp)

for x in range(len(str_tmp)):
    result += int(str_tmp[x])

print(result)