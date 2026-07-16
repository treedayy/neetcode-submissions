class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {}
        li = [[] for _ in range(9)]
        #for row in range(0, 3, 1):
        #    for col in range(0, 3, 1):
        #        li[0].append(board[row][col])
        for b in range(9):
            r_start = (b // 3) * 3
            c_start = (b % 3) * 3
            for row in range(0, 3, 1):
                for col in range(0, 3, 1):
                    if board[row+r_start][col+c_start] != '.':
                        li[b].append(board[row+r_start][col+c_start])
            if len(li[b]) != len(set(li[b])):
                return False
        rowli = [[] for _ in range(9)]
        colli = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rowli[r].append(board[r][c])
                if board[c][r] != '.':
                    colli[r].append(board[c][r])
            if len(rowli[r]) != len(set(rowli[r])):
                return False
        
        for c in range(9):
            if len(colli[c]) != len(set(colli[c])):
                return False

        #print(li)
        return True