word_lists=["Lovely Runner","Queen Of Tears","Twinkling Watermelon","Crash landing on you","Business proposal","All Of Us Are Dead"]
import random
random_choice=random.choice(word_lists)
print(word_lists)
chance=5
while chance>0:
    chance-=1
    user_guess=input("Guess My Fav K-drama on the above lists: ")
    if user_guess==random_choice:
        print("Your guess is right")
    else:
        print(" oops!Your guess is wrong")
