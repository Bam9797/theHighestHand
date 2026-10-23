
import random
import os
import Deck
import Enemies

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
    enemyPersonality=random.choice(Enemies.randomEnemies)
    enemy=Enemies.Enemy(enemyPersonality)
    enemy.Introduction(0)
    
    Round=1
    Win=0
    Lost=0
    
    while Round<=5 and Win<3 and Lost<3:
        while True:
            print("\n\nYour hand is: ", end="")
            print(*player.inHand(),sep=", ")
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
            enemy.Round(1)
        elif yourCard < Enemy.card:
            Lost += 1
            print("You lose this round!")
            enemy.Round(-1)
        else:
            print("It's a tie!")
            enemy.Round(0)
        Round += 1
    finalResults(Win, Lost, Round)
    replay()

def finalResults(win, lost, round, Enem=Enemies.Enemy(random.choice(Enemies.randomEnemies))):
    print(f"\nFinal Results:\nWins: {win}\nLosses: {lost}\nRounds Played: {round-1}\n\n")
    if win > lost:
        Enem.Win()
        print("Congratulations! You won the game!")
    elif win < lost:
        Enem.Lost()
        print("Sorry, you lost the game.")
    else:
        print("The game ended in a tie...")

def replay():
    match input("\nDo you want to play again? (y/n): "):
        case "y":
            game()
        case "n":
            print("Goodbye!\n")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            replay()




main()