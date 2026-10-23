
import random
import os
import Deck

def main():
    match input("\nWelcome to Highest hand.\n\nDo you want to play (y/n)?"):
        case "y":
            game()
        case "n":
            print("Goodbye!")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            main()
def game():
    player=Deck.Deck()
    Enemy=Deck.Deck()
    
    
    Round=1
    Win=0
    Lost=0
    
    while Round<=5 and Win<3 and Lost<3:
        print("Your hand is: ", player.inHand())
        yourCard = int(input(f"Round {Round}:\nChoose a card to play: "))
        Enemy.card = random.choice(Enemy.inHand())
        
        print(f"Your card: {yourCard}")
        print(f"Enemy's card: {Enemy.card}")
        if yourCard > Enemy.card:
            Win += 1
            print("You win this round!")
        elif yourCard < Enemy.card:
            Lost += 1
            print("You lose this round!")
        else:
            print("It's a tie!")
        Round += 1
    finalResults(Win, Lost, Round)
    replay()

def finalResults(win, lost, round):
    print(f"Final Results:\nWins: {win}\nLosses: {lost}\nRounds Played: {round-1}")
    if win > lost:
        print("Congratulations! You won the game!")
    elif win < lost:
        print("Sorry, you lost the game.")
    else:
        print("The game ended in a tie.")

main()

def replay():
    match input("Do you want to play again? (y/n): "):
        case "y":
            game()
        case "n":
            print("Goodbye!")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            replay()