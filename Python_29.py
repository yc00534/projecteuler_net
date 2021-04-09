arr = []


def function(x):
    global arr
    for i in range(2, 101):
        arr.append(x ** i)


for y in range(2,101):
    function(y)

arr = list(dict.fromkeys(arr))
arr.sort()
print(len(arr))
