print("pick your vehicle")
print("1-bike")
print("2-car")
choice=int(input("enter 1 or 2"))
print()
if choice==1:
    print("pick your bike type")
    print("1-scooty")
    print("2-mountain bike")
    print()
    
    biketype=int(input("enter 1 or 2"))
    print()

    if biketype==1:
        print("you picked scooty")

    else:
        print("you picked mountian bike")
elif choice==2:
    print("pick your car type")
    print("1-tesla")
    print("2-mistubushi")
    print()
    
    cartype=int(input("enter 1 or 2"))
    print()

    if cartype==1:
        print("you picked tesla")

    else:
        print("you picked mistubushi")
else:
    print("you have choosen incorrect statement")