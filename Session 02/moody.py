# random tu 0 den 100 
# neu lon hon 60, cam xuc tot
# duoi 30, toi te
from random import randint
mood = randint(0, 100)
print(mood)

if mood<30: 
    print("T.T")
elif mood<60:
    print('._.')
else :
    print("Let rock")