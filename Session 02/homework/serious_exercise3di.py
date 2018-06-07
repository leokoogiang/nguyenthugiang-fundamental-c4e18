# for i in range(0,10):
#     for j in range(0,10,2):
#         print('1', end=' ')
#         print('0', end=' ')
#     print()


for i in range(10):
    for j in range(10):
        if (i%2 and j%2) or (i%2==0 and j%2==0):
            print('1', end = '\t')
        else:
                 print('0', end = '\t')
    print()