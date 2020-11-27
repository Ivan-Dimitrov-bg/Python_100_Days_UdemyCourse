# _____________________________
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
#from art import logo


#def display_logo():
    #print(logo)
import random

def pick_a_cards(currScore):
        '''Return a random card'''
        list_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(list_cards)
        if card == 11:
            if currScore + 11 > 21:
                card = 1
            else:
                card = 11
        return card


def computer_pick_cards(computer_cardss):
    while sum(computer_cardss) < 17 and sum(computer_cardss) != 21:
            computer_cardss.append(pick_a_cards(sum(computer_cardss)))

    return computer_cardss


play_starts = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))

while play_starts == 'y':
   # display_logo()
    game_in_progress = True
    player_cards = []
    computer_cards = []
    player_cards.append(pick_a_cards(sum(player_cards)))
    computer_cards.append(pick_a_cards(sum(computer_cards)))


    more_cards_1 = "y"
    first_run = True
    if more_cards_1 == "n":
        computer_cards = computer_pick_cards(computer_cards[0], sum(player_cards))
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    else:
        while more_cards_1 == "y":
            # clear()
            player_cards.append(pick_a_cards(sum(player_cards)))
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"  Computer's first card: {computer_cards[0]}")
            if sum(player_cards) > 21:
                break
            more_cards_1 = input(f"Type 'y' to get another card, type 'n' to pass:")

        if more_cards_1 == "n":
            computer_cards = computer_pick_cards(computer_cards)
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    if sum(player_cards) > 21:
        print("You went over. You lose 😭")
    elif sum(computer_cards) > sum(player_cards) and sum(computer_cards) < 21:
        print("You lose 😭")
    elif sum(computer_cards) < sum(player_cards):
        print("Win with a Blackjack 😎")
    elif sum(computer_cards) == sum(player_cards):
        print("Draw 🙃")

    play_starts = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))