c = 0
for x in range(-200, 200):
    for y in range(200):
        if x < 0 and y > -15*x/(675**0.5) and (y - 15) / 15 < ((x + (675**0.5))/(675**0.5)):
            c += 1
print(c)