############### Blackjack Project #####################

############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def play():
    current_score_player = 0
    cards_count = random.randint(0, 12)
    # print(cards_count)
    player_hand = []
    player_hand.append(cards[cards_count])
    cards_count = random.randint(0, 12)
    player_hand.append(cards[cards_count])
    for i in player_hand:
        current_score_player += i
    computer_hand = []
    computer_hand.append(cards[cards_count])
    current_score_comp = 0
    for i in computer_hand:
        current_score_comp += i


    if current_score_player >= 22:
        print("You lose you are already above 21 !")
    else:
        print(f"Your cards: {player_hand}, current score: {current_score_player}")
        print(f"Computer's first card: {current_score_comp}")

        get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        get_another_card = False

        if get_card == "y":
            # print("You can't finish game if yours current score is below 17 ")
            get_another_card = True
            while get_another_card == True:
                cards_count = random.randint(0, 12)
                player_hand.append(cards[cards_count])
                # print(player_hand)
                current_score_player = 0
                for i in player_hand:
                    current_score_player += i
                computer_hand.append(cards[cards_count])
                current_score_comp = 0
                for i in computer_hand:
                    current_score_comp += i
                # print(current_score_player)
                # print(computer_hand)
                #print(current_score_comp)
                print(f"Your cards: {player_hand}, current score: {current_score_player}")
                print(f"Computer's first card: {computer_hand[0]}")
                get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if get_card == "y":
                    get_another_card = True
                else:
                    if current_score_player < 17:
                        print("You can't finish game if yours current score is below 17 ")
                        get_another_card = True
                    else:
                        get_another_card = False
                        print(f"Your final hand: {player_hand}, final score: {current_score_player}")
                        print(f"Computer's final hand: {computer_hand}, final score: {current_score_comp}")
                        if current_score_player > 21:
                            print("You lose!, you have score greater than max 21!")
                        elif current_score_comp > 21:
                            print("You win!, Computer have score greater than max 21!")
                        elif current_score_player > current_score_comp:
                            print("You win!")
                        elif current_score_comp > current_score_player:
                            print("You lose!")
                        elif current_score_comp == current_score_player:
                            print("You draw!")
                        play_again = input("Do you want to play again ? Type 'y' or 'n'. ").lower()
                        if play_again == "y":
                            play()
        else:
            if current_score_player < 17:
                get_another_card = True
                print("You can't end game if your's score is below 17! ypu must take card!")
                while get_another_card == True:
                    cards_count = random.randint(0, 12)
                    player_hand.append(cards[cards_count])
                    # print(player_hand)
                    current_score_player = 0
                    for i in player_hand:
                        current_score_player += i
                    computer_hand.append(cards[cards_count])
                    current_score_comp = 0
                    for i in computer_hand:
                        current_score_comp += i
                    print(current_score_player)
                    # print(computer_hand)
                    # print(current_score_comp)
                    print(f"Your cards: {player_hand}, current score: {current_score_player}")
                    print(f"Computer's first card: {computer_hand[0]}")
                    get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if get_card == "y":
                        get_another_card = True
                    else:
                        if current_score_player < 17:
                            print("You can't finish game if yours current score is below 17 ")
                            get_another_card = True
                        else:
                            get_another_card = False
                            print(f"Your final hand: {player_hand}, final score: {current_score_player}")
                            print(f"Computer's final hand: {computer_hand}, final score: {current_score_comp}")
                            if current_score_player > 21:
                                print("You lose!, you have score greater than max 21!")
                            elif current_score_comp > 21:
                                print("You win!, Computer have score greater than max 21!")
                            elif current_score_player > current_score_comp:
                                print("You win!")
                            elif current_score_comp > current_score_player:
                                print("You lose!")
                            elif current_score_comp == current_score_player:
                                print("You draw!")
                            play_again = input("Do you want to play again ? Type 'y' or 'n'. ").lower()
                            if play_again == "y":
                                play()
            else:
                get_another_card = False
                print(f"Your final hand: {player_hand}, final score: {current_score_player}")
                print(f"Computer's final hand: {computer_hand}, final score: {current_score_comp}")
                if current_score_player > 21:
                    print("You lose!, you have score greater than max 21!")
                elif current_score_comp > 21:
                    print("You win!, Computer have score greater than max 21!")
                elif current_score_player > current_score_comp:
                    print("You win!")
                elif current_score_comp > current_score_player:
                    print("You lose!")
                elif current_score_comp == current_score_player:
                    print("You draw!")
                play_again = input("Do you want to play again ? Type 'y' or 'n'. ").lower()
                if play_again == "y":
                    play()



play()
