# create a dictinary with folowers
# pick randomly form a dictionary
# ask the user
# display the result
# ask again
# game over

import pandas as pd
import random


class Celebrity:
    name = ""
    followers = 0
    description = ""
    picked = False

    def __init__(self, name, followers, description):
        self.name = name
        self.followers = int(followers)
        self.description = description
        self.picked = False

    def __str__(self):
        return (f"{self.name} | {self.followers} | {self.description}")

def InitSettings():
    df = pd.read_excel('Followers.xlsx', 'Sheet1')

    #df = df.where(pd.notnull(df), None)

    collection_all_celebrity = []

    for (n, s, d) in df.values:
        collection_all_celebrity.append(Celebrity(n, s, d))

    return collection_all_celebrity

    #for r in collection_all_celebrity:
        #print(r)

def pickCelebrity(celebrities):
    currCelebrity = random.choice(celebrities)
    currCelebrity.picked = True
    return currCelebrity

def ask_user_to_choise(selebrity_one, selebrity_two):
    print(f"Compare A: {selebrity_one.name} => {selebrity_one.description} ")
    print("VS")
    print(f"Against B: {selebrity_two.name} => {selebrity_two.description} ")
    userInput = input("Who has more followers? 'A' or 'B': ")
    if userInput == 'A' and selebrity_one.followers >= selebrity_two.followers:
        return True
    elif userInput == 'B' and selebrity_one.followers <= selebrity_two.followers:
        return True
    else:
        return False


def start():
    celebrities = InitSettings()

    selebrity_one = pickCelebrity(celebrities)
    user_guess_right = True
    score = 0
    while user_guess_right:
        selebrity_two = pickCelebrity(celebrities)
        user_guess_right = ask_user_to_choise(selebrity_one, selebrity_two)
        if user_guess_right:
            score += 1
            print(f"Good job your score is: {score}")
            selebrity_one = selebrity_two
        else:
            start_again = print("That wasn't right. Do you like to start again? Y / N")
            if start_again== "Y":
                user_choice = True
                score = 0

start()


#od = co.OrderedDict((k.strip().encode('utf8'), v.strip().encode('utf8')) for (k, v) in df.values)
