import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("Enter a choice(rock,paper,scissors): ").lower()
    print("Player: ", player)
    print("Computer: ", computer)

    if player == computer:
      print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
      print("You Win!")
    elif player == "paper" and computer == "rock":
      print("You Win!")
    elif player == "scissors" and computer == "paper":
      print("You Win!")
    else:
      print("You Lose!")

    again = input("Would you like to play again(y/n)? : ").lower()
    if again != 'y':
      playing = False

print("Thanks for playing!!!")
