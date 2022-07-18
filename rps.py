"""
For this project, you will individually create a program that has a "player" and a "computer" advisary. 
The computer should randomly choose it's decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). 
The player should then have a chance to input their decision. If player and computer choose the same decision then display ("Game Tied"), 
If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), if the player chooses "Scissors" and the computer chooses "Rock" 
display ("You Lose") and if the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") -- Vice versa for other descisions. 

Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").

In this project, you will need to use the random.randint function to enable to computer to make a random decision. 
Full documentation on the use of this function is attached in a link to this assignment.
"""

import random

class RockPaperScissors:
    
    def __init__(self):

        #scoreboard to keep track of scores
        self.scoreboard = { "tie": 0,
                            "win": 0,
                            "loss": 0,
        }
        

        self.rps = {'rock': 0, 
                    'paper': 1, 
                    'scissors': 2,
        }

    def conditions(self, player, computer):

        # This formula will always return 0-2
        # Both player and computer will get numeric from self.rps
        result = (player - computer) % 3
        if result == 0:
            self.scoreboard["tie"] += 1
            print("Game Tied!")
        elif result == 1:
            self.scoreboard["win"] += 1
            print("You win!")
        elif result == 2:
            self.scoreboard["loss"] += 1
            print("You Lose!")


    def run_simulation(self):

        while True:
            player_choice = input("Rock, Paper or Scissors? ").lower()
            if player_choice in self.rps.keys():
                break
            print("Invalid input, try again!")
        

        computer_choice = random.choice(list(self.rps.keys()))
        print(f"You've picked {player_choice}, and computer picked {computer_choice}.")

        # comparison of player and computer rps to see who won based on conditions
        self.conditions(self.rps[player_choice], self.rps[computer_choice])
        print(f"\nThis is the result so far: {self.scoreboard}")


def run():
    game = RockPaperScissors()
    while True:
        game.run_simulation()

        while True:
            userInput = input("\nDo you wish to coninue? Type 'yes' or 'I quit' : ").lower()
            if userInput == 'i quit':
                print("Thank you for playing!")
                exit()
            elif userInput == 'yes':
                break
            else:
                print("Invalid input!\n")
                continue
            
run()