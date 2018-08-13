player1 = input("Player 1 Choose: rock , paper , scissors.. ? ")
player2 = input("Player 2 Choose: rock , paper , scissors.. ? ")
def play(player1, player2):
    if player1 == player2:
        print("Oops! It's a tie")
    elif player1 == 'rock':
        if player2 == 'scissors':
            return ("Player 1 wins!")
        else:
            return ("Player 2 wins!")
    elif player1 == 'scissors':
        if player2 == 'paper':
            return ("Player 1 wins!")
        else:
            return ("Player 2 wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            return ("Player 1 wins!")
        else:
            return ("Player 2 wins!")
    else:
        return ("Wrong choice\n")


s=play(player1,player2)
print(s)