from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            cur, dist = queue.popleft()
            for i in range(len(beginWord)):
                for j in range(26):
                    nxt = cur[:i] + chr(97+j) + cur[i+1:]
                    if nxt not in word_set:
                        continue
                    if nxt == endWord:
                        return dist+1
                    word_set.remove(nxt)
                    queue.append((nxt, dist+1))
        return 0


if __name__ == "__main__":
    sol = Solution()
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(begin_word, end_word, word_list))
