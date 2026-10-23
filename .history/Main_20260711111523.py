def main():
    match input("Welcome to Highest hand.\n\nDo you want to play (y/n)?"):
        case "y":
            NewGame()
        case "n":
            print("Goodbye!")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            main()

