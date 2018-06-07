day_so = [9, 8, 6, 7, 12]
length = len(day_so)
for j in range(0, length - 1):
    for i in range(0, length -1 -j):
        if day_so[i] > day_so[i+1]:
            day_so[i], day_so[i+1] = day_so[i+1], day_so[i]
print('The sorted list is: ', day_so)