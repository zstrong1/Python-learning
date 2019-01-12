age = 18
Tag = True
answer = ""
while(Tag):
    for i in range(3):
        print("Guass the age:")
        guass_age = int(input())
        if guass_age == age:
            print("You are right,Game Over!")
            Tag = False
            break
        else:
            print("Wrong,again")
    if Tag :
         print("Continue or stop, y or n")
         answer = input()
         if answer == 'N' or answer == 'n':
             print("Game Over,You Lose")
             break



