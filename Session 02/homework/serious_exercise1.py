print("Hello guy!") # Say hello
height = int(input("What is your height (in cm)?"))
weight = int(input("What is your weight (in kg)?"))
BMI = weight/((height/100)**2)
print(BMI)

if BMI<=16:
    print('You are severly underweight')
elif (BMI>16 and BMI<=18.5):
    print('You are underweight')
elif (BMI>18.5 and BMI<=25):
    print('You are normal')
elif (BMI>25 and BMI<=30):
    print('You are overweight')
else:
    print('You are obese')

