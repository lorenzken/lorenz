
def remarks(rem):
    match rem:
        case "A":
            print("Excellent")
        case "B":
            print("Good job!")
        case "C":
            print("Needs improvemnt")
        case "D":
            print("Provation")
        case "F":
            print("Failed")
#number 1
def grading_system():
    print("Hello! This is an app to know your grade!^^ ")
    
    Grade=int(input("Please Enter Your grade here: "))
    absences=int(input("Please Enter How Many Absences you have: "))
    remark=""
    if Grade >=90 and Grade <=100:
       if absences <=5:
        remark="A"
        remarks(remark)
       elif absences >=5:
        print("You need to talk to your teacher ")
    elif Grade >=80 and Grade <=89:
        if absences <=5:
            remark="B"
            remarks(remark)
        elif absences >=5:
            print("You need to talk to your teacher ")
    elif Grade >=70 and Grade <=79:
        if absences <=5:
            remark="C"
            remarks(remark)
        elif absences >=5:
            print("You need to talk to your teacher ")
    elif Grade >=60 and Grade <=69:
        if absences <=5:
            remark="D"
            remarks(remark)
        elif absences >=5:
            print("YOU FAILED ")
    elif Grade <60:
        if absences <=5:
            remark="F"
            remarks(remark)
        elif absences >=5:
            print("YOU FAILED ")
#number 2
def exit():
    print("Thank you for using the app! ")
#main       
def main():
    while True:
        try:
            print("Hi, Welcome! What do you want to do? ")
            print("[1] Enter your grade and absences ")
            print("[2] exit ")

            Choices=int(input("Please select a choice from 1-2: "))
            match Choices:
                    case 1:
                        grading_system()
                        continue   
                    case 2:
                        exit()
                        break
                    case _:
                        print("Invalid output please choice only from 1-3 ")
                        continue
        except ValueError:
            print("Please enter a valid input: ")
    
main()

