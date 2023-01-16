board = list(range(1,10))
def drawBoard(board):
   for i in range(3): print(board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
def takeInput(playerToken):
   valid = False
   while not valid:
      playerAnswer = int(input("Ход " + playerToken+": "))
      if playerAnswer >= 1 and playerAnswer <= 9:
         if(str(board[playerAnswer - 1]) not in "XO"):
            board[playerAnswer - 1] = playerToken
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")
def checkWin(board):
   winCoord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in winCoord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False
counter = 0
win = False
while not win:
    drawBoard(board)
    if counter % 2 == 0:
       takeInput("X")
    else:
        takeInput("O")
    counter += 1
    if counter > 4:
        tmp = checkWin(board)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break
drawBoard(board)