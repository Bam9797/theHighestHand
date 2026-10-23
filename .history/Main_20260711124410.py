
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
    player=Deck.Deck([1,2,3,4,5])
    Enemy=Deck.Deck([1,2,3,4,5])
    
    
    Round=1
    Win=0
    Lost=0
    
    while Round<=5 and Win<3 and Lost<3:
        print("Your hand is: ", end="")
        print(*player.inHand(),sep=", ")
        while True:
            try:
                yourCard = int(input(f"\nRound {Round}:\nChoose a card to play: "))
                if yourCard not in player.inHand():
                    print("You don't have that card. Please choose a valid card.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        player.play(yourCard)
        
        Enemy.card = random.choice(Enemy.inHand())
        Enemy.play(Enemy.card)
        
        print(f"\nYour card: {yourCard}")
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
    print(f"\nFinal Results:\nWins: {win}\nLosses: {lost}\nRounds Played: {round-1}\n\n")
    if win > lost:
        print("Congratulations! You won the game!")
    elif win < lost:
        print("Sorry, you lost the game.")
    else:
        print("The game ended in a tie...")

def replay():
    match input("\nDo you want to play again? (y/n): "):
        case "y":
            game()
        case "n":
            print("Goodbye!")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            replay()

main()