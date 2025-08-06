#welcome message
print("welcome to the body weight calculator")

#Constants
UNDER = 18.5
NORMAL = 24.9
OVER = 29.9

#input info about the user
Name = input("Please enter your name: ")
Weight = float(input("Please enter your body weight in kg: "))
Height = float(input("Please enter your height in m: "))


#calculate bmi
BMI = Weight / (Height ** 2)

#conditions 
if( Weight <= 0 or Height <= 0):
    print("Please enter valid number for weight and height.")
else:
    if BMI <= UNDER:
        print(f"{Name}, your are underweight.")
    elif BMI <= NORMAL:
        print(f"{Name}, you have a normal weight.")
    elif BMI <= OVER:
        print(f"{Name}, you are overweight.")
    else:
        print(f"{Name} you are obese.")
          






