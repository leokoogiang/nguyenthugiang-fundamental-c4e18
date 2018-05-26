#for i in range(10): 
    #for j in range(i): #print one line
        #print('*', end='') # sau khi het 1 dong phai xuong dong
        # break 
    # print()

for i in range(10):
    for j in range(10):
        if j>=10 - i - 1:
            print('',end='')
        else:
            print('*', end='') 
    print()


