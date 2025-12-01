
from game import Game


def get_user_menu_choice() -> str:
    """
    Print the main menu once and return the user's choice:
    - "g" : play a new game
    - "s" : show scores
    - "q" : quit
    No looping should occur outside input validation of this function.
    """
    print("\n=== Rock - Paper - Scissors ===")
    print("(g) Play a new game")
    print("(s) Show scores")
    print("(q) Quit")

    valid_choices = {"g", "s", "q"}

    choice = input("Enter your choice (g/s/q): ").strip().lower()
    while choice not in valid_choices:
        print("Invalid choice. Please choose g, s or q.")
        choice = input("Enter your choice (g/s/q): ").strip().lower()

    return choice


def print_results(results: dict) -> None:
    """
    Print a summary of all games played.
    Expects a dictionary like: {"win": 2, "loss": 4, "draw": 3}
    """
    print("\n=== Game Summary ===")
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)
    total = wins + losses + draws

    print(f"Total games played: {total}")
    print(f"Wins :  {wins}")
    print(f"Losses: {losses}")
    print(f"Draws: {draws}")
    print("Thanks for playing Rock - Paper - Scissors!\n")


def main() -> None:
    """
    Main game loop:
    - Repeatedly show the menu until the user quits.
    - When playing a game, create a Game() object and call play().
    - Track all results in a dictionary and show them on quit.
    """
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "g":  # play a new game
            game = Game()
            result = game.play()
            # Update statistics
            if result in results:
                results[result] += 1

        elif choice == "s":  # show scores
            print_results(results)

        elif choice == "q":  # quit
            print_results(results)
            break


if __name__ == "__main__":
    main()
