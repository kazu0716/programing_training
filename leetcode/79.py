from functools import lru_cache
from sys import setrecursionlimit
from typing import List

setrecursionlimit(pow(10, 6))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(cur_i: int, cur_j: int, msg: str, pos: str) -> bool:
            res = False
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nxt_i, nxt_j = cur_i+di, cur_j+dj
                idx = nxt_i*len(board[0])+nxt_j
                if 0 <= nxt_i < len(board) and 0 <= nxt_j < len(board[0]) and board[nxt_i][nxt_j] == msg[0] and pos[idx] == "0":
                    if len(msg) <= 1:
                        return True
                    res = res or dfs(nxt_i, nxt_j, msg[1:], pos[:idx]+"1"+pos[idx+1:])
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    pos, idx = "0"*len(board)*len(board[0]), i*len(board[0])+j
                    if len(word) == 1 or dfs(i, j, word[1:], pos[:idx]+"1"+pos[idx+1:]):
                        return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
    word = "AAAAAAAAAAAABAA"
    print(sol.exist(board, word))
