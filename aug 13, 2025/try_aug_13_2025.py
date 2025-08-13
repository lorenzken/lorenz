#age input

while True:
    try:
        age = int(input("Please enter your age:"))
                    
        if age < 0:
            print("age must be inside 0 - 100")
            continue
        elif age > 100:
            print("age must be inside 0 - 100")
            continue
        print(age)
        break
        
        
    except ValueError:
        print("Invalid input")
        continue
   


