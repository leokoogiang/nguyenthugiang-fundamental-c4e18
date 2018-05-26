# camel case vs snake case: yearOfBirth, year_of_birth (python case)
yob = int(input('What is your yob? ' ))

age = 2018 - yob

# Cau truc re nhanh, cau truc dieu kien, chay tung lenh, chay tu tren xuong duoi, khi dung if, may tinh se re nhanh
# sau if se la 1 dieu kien
# da di vao 1 nhanh se khong di sang nhanh khac


if age < 10: 
    print('Baby')
elif age <= 18: # hoac la age<19
    print('Teenager')

elif age==24: # '=' nghia la gan
    print('Lay chong thoi')

else: # neu khong thi
    print('Not baby')

print('Bye')