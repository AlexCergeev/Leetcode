class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                el = board[i][j]
                if el == '.':
                    continue
                if (el in rows[i] or el in cols[j] 
                    or el in squares[(i//3, j//3)]):
                    return False
                rows[i].add(el)
                cols[j].add(el)
                squares[(i//3, j//3)].add(el)
        return True