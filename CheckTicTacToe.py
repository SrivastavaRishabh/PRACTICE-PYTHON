def play(mark):
    winner = {0: " draw ", 1: " player 1", 2: " player 2"}
    for i in range(1, 3):
        if mark[0] == [i, i, i] or mark[1] == [i, i, i] or mark[2] == [i, i, i]:
            return winner[i]
        elif mark[0][0] == i and mark[1][0] == i and mark[2][0] == i:
            return winner[i]
        elif mark[0][1] == i and mark[1][1] == i and mark[2][1] == i:
            return winner[i]
        elif mark[0][2] == i and mark[1][2] == i and mark[2][2] == i:
            return  winner[i]
        elif mark[0][0] == i and mark[1][1] == i and mark[2][2] == i:
            return winner[i]
        elif mark[0][2] == i and mark[1][1] == i and mark[2][0] == i:
            return winner[i]
        else:
            return winner[0]


print(" Tic Tac Toe ")
print(" Board size 3")
print(" Player One enter 1 ")
print(" Player Two enter 2 ")
game = []
for i in range(0, 3):
   game.append([])
   for j in range(0, 3):
       game[i].append(int(input(" Enter for position %s,%s : " %(i+1, j+1))))
print("Marked places : ", game)
print(" Results : ", play(game))
