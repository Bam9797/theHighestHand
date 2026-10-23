
import random
import os
import Deck

def main():
    match input("\nWelcome to Highest hand.\n\nDo you want to play (y/n)?"):
        case "y":
            NewGame()
        case "n":
            print("Goodbye!")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            main()
def NewGame():
    player=Deck.Deck([1,2,3,4,5])
    Enemy=Deck.Deck([1,2,3,4,5])
    print("Your hand is: ", player.inHand())
    Round=1
    Win=0
    Lost=0
    while Round<=5 and Win<3 and Lost<3:
        YourCard = int(input(f"Round {Round}:\nChoose a card to play: "))
        Enemy.card = random.choice(Enemy.inHand())
        print(f"Your card: {YourCard}")
        print(f"Enemy's card: {Enemy.card}")
        if YourCard > Enemy.card:
            Win += 1
            print("You win this round!")
        elif YourCard < Enemy.card:
            Lost += 1
            print("You lose this round!")
        else:
            print("It's a tie!")
        Round += 1
    if Win > Lost:
        print("Congratulations! You won the game!")
    elif Win < Lost:
        print("Sorry, you lost the game.")
    else:
        print("The game ended in a tie.")
    
    match input("Do you want to play again? (y/n): "):
        case "y":
            NewGame()
        case "n":
            print("Goodbye!")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            main()
main()