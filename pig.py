import random

players = input("Enter the number of players (2 : 4)")

def roll_dice():
    max_value = 6
    min_value = 1
    roll_value = random.randint(min_value, max_value)

    return roll_value


while True:
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break

        else:
            print("Players must be from 2 to 4")   
        
    else:
        print("Enter valid number of players")
        

        
player_score = [0] * players

print(player_score)

player_index = 1

flag = True

while flag:
    while player_index < players + 1:
        max_score = 50
        total_score = player_score[player_index-1]
        
        while player_score[player_index-1] < max_score:
            print(f"Player: {player_index}")
            print(f"Total score for player:{player_index} is {total_score}")
            decider = input("y for Roll n for Settle")

            if decider.lower() == "y":
                value = roll_dice()

                if value == 1:
                    total_score = 0
                    player_score[player_index-1] = total_score
                    break
                total_score = total_score +  value
                player_score[player_index-1] = total_score

                if total_score >= max_score:
                    print(f"Congratulations player {player_index}, you just won!!")
                    flag = False
                    break

                

            else:
                break

        
            
        player_index = player_index + 1   
    player_index = 1 


