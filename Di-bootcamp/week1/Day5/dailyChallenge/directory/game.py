
import random


class Game:
    VALID_ITEMS = ("rock", "paper", "scissors")

    def get_user_item(self) -> str:
        """
        Ask the user to select rock / paper / scissors.
        Keep asking until a valid choice is made.
        Returns the full word: "rock", "paper" or "scissors".
        """
        abbreviations = {
            "r": "rock",
            "p": "paper",
            "s": "scissors",
        }

        while True:
            user_input = input("Choose (r)ock, (p)aper or (s)cissors: ").strip().lower()

            # Allow both full words and single-letter shortcuts
            if user_input in self.VALID_ITEMS:
                return user_input
            if user_input in abbreviations:
                return abbreviations[user_input]

            print("Invalid choice. Please type rock/paper/scissors or r/p/s.")

    def get_computer_item(self) -> str:
        """
        Randomly select rock / paper / scissors for the computer.
        """
        return random.choice(self.VALID_ITEMS)

    def get_game_result(self, user_item: str, computer_item: str) -> str:
        """
        Determine the game result from the user perspective.
        Returns: "win", "loss" or "draw".
        """
        if user_item == computer_item:
            return "draw"

        # Winning combinations for the user
        winning_combos = {
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper"),
        }

        if (user_item, computer_item) in winning_combos:
            return "win"
        else:
            return "loss"

    def play(self) -> str:
        """
        Play one full game round:
        - get user item
        - get computer item
        - compute result
        Print a friendly message and return the result string:
        "win", "loss" or "draw".
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # Build result sentence
        if result == "win":
            message = "You win!"
        elif result == "loss":
            message = "You lose!"
        else:
            message = "It's a draw!"

        print(f"You selected {user_item}. The computer selected {computer_item}. {message}")
        return result
