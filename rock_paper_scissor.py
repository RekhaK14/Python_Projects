print("\t\t\t\tR O C K  P A P E R  S C I S S O R")
print()
print("\t\t\t\tTOTAL CHANCES:10")
print("\t\t\t\tLet's play")
import random
user_wins=0
computer_wins=0
tied=0
chance=10
while chance>0:
    chance-=1
    user_choice=input("\t\t\t\trock/paper/scissor: ").lower()
    choice=['rock','paper','scissor']
    random_choice=random.randint(0,2)
    computer_choice=choice[random_choice]
    print("\t\t\t\tComputer Chose:",computer_choice)
    if user_choice=="rock" and computer_choice=="scissor":
        print("\t\t\t\tYou won")
        user_wins+=1
    elif user_choice=="paper" and computer_choice=="rock":
        print("\t\t\t\tyou won")
        user_wins+=1
    elif user_choice=="scissor" and computer_choice=="paper":
        print("\t\t\t\tyou won")
        user_wins+=1
    elif user_choice==computer_choice:
        print("\t\t\t\tYou both got tied")
        tied+=1
    else:
        print("\t\t\t\tComputer won")
        computer_wins+=1
print("\t\t\t\t####################################")
print("\t\t\t\tYou won",user_wins,"times")
print("\t\t\t\tComputer won",computer_wins,"times")
print("\t\t\t\tyou both got tied at",tied,"times")
print()

if user_wins>computer_wins:
    print("\t\t\t\tYou won the game!!!!!!!!")
elif user_wins==computer_wins:
    print("\t\t\t\tYou both got same points")
else:
    print("\t\t\t\tComputer won the game!!!!!!!!!!")
print("\t\t\t\t####################################")
