a, b = 0, 1
result = 0

while True:
    a, b = b, a + b
    if result < 4000000:
        if b % 2 == 0:
            result += b
    else:
        break

print("Answer: ", result)