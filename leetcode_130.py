class Solution(object):
    def solve(self, board):
        r = len(board)
        if r==0:
            return []
        c = len(board[0])
        if c==0:
            return []

        def markNonPerformingZero(i,j):
            try:
                if board[i][j]=="M":
                    return
                if board[i][j]=="X":
                    return
                elif board[i][j]=="O":
                    board[i][j]="M"
            except:
                return

            markNonPerformingZero(i,j+1)
            markNonPerformingZero(i,j-1)
            markNonPerformingZero(i+1,j)
            markNonPerformingZero(i-1,j)


        for k in range(c):
            if board[0][k]=="O":
                markNonPerformingZero(0,k)

            if board[r-1][k]=="O":
                markNonPerformingZero(r-1,k)

        for m in range(r):
            if board[m][0]=="O":
                markNonPerformingZero(m,0)

            if board[m][c-1]=="O":
                markNonPerformingZero(m,c-1)


        for i in range(r):
            for j in range(c):
                if board[i][j]=="M":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"

        return board
