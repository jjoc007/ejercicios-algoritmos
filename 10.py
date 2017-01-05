games = int(raw_input())

boardLetters = {'A':0,'B':1,'C':2,'D':3}
board = []

def clearBoard():
    for i in range(0,4):
        row = []
        for j in range(0,4):
            row.append('')
        board.append(row)

for g in range(0,games):

    parameters = map(int, raw_input().split(' '))
    clearBoard()

    #fill p white
    for w in range(0,parameters[0]):
        piece = raw_input().split(' ')
        board[4-int(piece[2])][ int(boardLetters[ piece[1]] )] = str(piece[0])+'W'



    #fill p black
    for w in range(0,parameters[1]):
        piece = raw_input().split(' ')
        board[4-int(piece[2])][ int(boardLetters[ piece[1]] )] = str(piece[0])+'B'

    print (board)
