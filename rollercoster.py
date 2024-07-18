#roller coster bill method
height = int(input("enter the height of the person"))
bill = 0
if height > 120:
    print("You can ride")
    age = int(input("enter the age"))
    if age <= 12:
        bill = 5
        print("child tickets are 5$ ")
    elif age <=18 :
        bill = 7
        print("youth tickets are 7$")
    elif age >= 45 and age <= 55:
        print("Every thing is going to be ok. Have a free ride on us! ")  
    else:
        bill = 12
        print("adult tickets are 12$")  
    ask_photo = input('do you want to take photo "y" "N" ')   
    if ask_photo == "y" :
        bill += 3
    print(f"total bill is {bill}")       
else:
    print("sorry you need to grow up ")      