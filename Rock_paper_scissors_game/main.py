import random

c=["paper","rock","scissors"]

player_score=0
pc_score=0

while True:

    pc_choice=random.choice(c)

    player_choice=input("Paper, Rock or Scissors? ")

    if player_choice=="stop" or player_choice=="end":
        print("Game ended!")
        print("Final score:")
        print("PC score: ",pc_score)
        print("Player score",player_score)
        break

    elif pc_choice=="paper" and player_choice=="paper":
        print("Tie!")
        pc_score+=1
        player_score+=1

    elif pc_choice=="rock" and player_choice=="rock":
        print("Tie!")

    elif pc_choice=="scissors" and player_choice=="scissors":
        print("Tie!")

    elif pc_choice=="paper":
        if player_choice=="rock":
            pc_score+=1
            print("You choose rock and PC choose paper. PC wins.")
        elif player_choice == "scissors":
            player_score+=1
            print("You choose scissors and PC choose paper. You win.")

    elif pc_choice=="rock":
        if player_choice=="paper":
            player_score+=1
            print("You choose paper and PC choose rock. You win.")
        elif player_choice=="scissors":
            pc_score+=1
            print("You choose scissors and PC choose rock. PC wins.")

    elif pc_choice=="scissors":
        if player_choice=="paper":
            pc_score+=1
            print("You choose paper and PC choose scissors. PC wins.")
        elif player_choice=="rock":
            player_score+=1
            print("You choose rock and PC choose scissors. You win.")
   
