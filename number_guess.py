print("\t\t\t\tN U M B E R  G U E S S I N G  G A M E ")
print()
import random
random_number=random.randint(1,5)
chance=10
while chance>0:
    user_guess=int(input("\t\t\t\tGuess a number: "))
    if user_guess==random_number:
        print("\t\t\t\tYou guessed the correct number")
        q_c=input("\t\t\t\twant to continue or quit enter c to continue or q to quit: ")
        if q_c=="q":
            quit()
        else:
            continue
    elif user_guess>random_number:
        print("\t\t\t\tToo High")
    elif user_guess<random_number:
        print("\t\t\t\tToo Low")

