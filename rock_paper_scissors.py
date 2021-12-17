import random

computer_score = 0
player_score = 0
print('The name of the game is Rock, Paper, Scissors! Best to 3 wins!')

while True:
    player = input('Make your choice- rock, paper, or scissors?  ').lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if player == computer:
        print('You both chose ' + player + '! ' 'Looks like a tie!')
# player chooses rock
    elif player == 'rock' and computer == 'scissors':
        print('Rock smashes scissors. You win this round!')
        player_score += 1
        print('Player: ' + str(player_score) + ' Computer: ' + str(computer_score))
    elif player == 'rock' and computer == 'paper':
        print('Paper covers rock. Computer wins this round.')
        computer_score += 1
        print('Player: ' + str(player_score) + ' Computer: ' + str(computer_score))
# player chooses paper
    elif player == 'paper' and computer == 'rock':
        print('Paper cover rock. You win this round!')
        player_score += 1
        print('Player: ' + str(player_score) + ' Computer: ' + str(computer_score))
    elif player == 'paper' and computer == 'scissors':
        print('Scissors cuts paper. Computer wins this round.')
        computer_score += 1
        print('Player: ' + str(player_score) + ' Computer: ' + str(computer_score))
# player chooses scissors
    elif player == 'scissors' and computer == 'paper':
        print('Scissors cuts paper. You win this round!')
        player_score += 1
        print('Player: ' + str(player_score) + ' Computer: ' + str(computer_score))
    elif player == 'scissors' and computer == 'rock':
        print('Rock smashes scissors. Computer wins this round.')
        computer_score += 1
        print('Player: ' + str(player_score) + ' Computer: ' + str(computer_score))
    else:
        print('Invalid entry. Try again!')
# winner
    if player_score == 3:
        print('You win!')
        break
    elif computer_score == 3:
        print('Computer wins!')
        break