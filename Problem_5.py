sensor = []
tmp = 0
zahlX = 0


def zahl(zahlX):
    for x in range(1, 11):
        if zahlX % x == 0:
            sensor.append(1)
        else:
            sensor.append(0)


for elem in sensor:
    tmp += elem

if tmp == 10:
    print(zahlX)

for i in range(1, 3000):
    zahl(i)
