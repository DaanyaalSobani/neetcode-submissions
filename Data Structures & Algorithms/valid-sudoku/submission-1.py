class Solution:
    def square_gen(self,board: List[List[str]]) -> Iterator[list[str]]:
        square_starts_r = [0,0,0,3,3,3,6,6,6]
        square_starts_c = [0,3,6,0,3,6,0,3,6]
        for i in range(len(board)):
            square_start_r,square_start_y = square_starts_r[i],square_starts_c[i]
            yield [board[square_start_r][square_start_y],
                   board[square_start_r+1][square_start_y],
                   board[square_start_r+2][square_start_y],
                   board[square_start_r][square_start_y+1],
                   board[square_start_r+1][square_start_y+1],
                   board[square_start_r+2][square_start_y+1],
                   board[square_start_r][square_start_y+2],
                   board[square_start_r+1][square_start_y+2],
                   board[square_start_r+2][square_start_y+2] 
            ]


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        for col_index in range(len(board)):
            seen = set()
            for row_index in range(len(board)):
                cell = board[row_index][col_index]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        for square in self.square_gen(board):
            print(square)
            seen = set()
            for cell in square:
                if cell == ".":
                    continue    
                if cell in seen:
                    return False
                seen.add(cell)
        return True