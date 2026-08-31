totalchores=4 
origianalcount=totalchores
print(f"you have {origianalcount}chores to finish today\n")
compleatedcount=0
chorenum=1
while chorenum<=totalchores:
    if chorenum==1: nextchore="make your beds"
    elif chorenum==2: nextchore="feed the pet"
    elif chorenum==3: nextchore="take out the trash"  
    else : nextchore="wash the dishes"
    answer=input(f"have you finished{nextchore}(yes/no)")
    if answer=="yes":
        compleatedcount+=1
        chorenum+=1
        print("great job chore copmleated ")
    else:
        print("ok finish it and check again")

    print("chorees remaining",totalchores-compleatedcount,totalchores,compleatedcount)
print("all chores compelete")
print("great work finishing your entireaere checklist today!\n")
#infinte loop 
print("now lets safely peak at and infinite loop")
test_value = 0
safety_counter = 0
while test_value <=0:
    print("this contiudton never changes so trthis would run forever")
    safety_counter +=1
    if safety_counter==3:
        print("stopping here on purpose- a real infonight loop never stops on its own")
        break
print("chore checklist summon")
print("chores assinied today", origianalcount)
print("chores compleeleted", compleatedcount)
print("chores remianing",totalchores- compleatedcount)
