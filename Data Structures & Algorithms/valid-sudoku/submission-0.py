class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = columns = 9

        # Verify column
        for i in range(columns):
            col_set = set()
            for j in range(rows):
                c = board[j][i]
                if c == '.':
                    continue
                if c in col_set:
                    return False
                col_set.add(c)
        print('=-=-=-=-=-=-=-=-=-=--')
        # Verify column
        for i in range(columns):
            col_set = set()
            for j in range(rows):
                c = board[i][j]
                if c == '.':
                    continue
                if c in col_set:
                    return False
                col_set.add(c)
        # Check squares
        for r0 in range(0, 9, 3):       # 0,3,6
            for c0 in range(0, 9, 3):   # 0,3,6
                seen = set()
                for r in range(r0, r0 + 3):
                    for c in range(c0, c0 + 3):
                        v = board[r][c]
                        if v == '.':
                            continue
                        if v in seen:
                            return False
                        seen.add(v)
        return True
