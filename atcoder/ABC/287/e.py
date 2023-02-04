from collections import defaultdict


class TrieNode:
    def __init__(self):
        # NOTE: don't need to handle index of string, because TrieNodes are different by key and index of string
        self.children = defaultdict(TrieNode)
        self.depth = 0
        self.num_set = set()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, num: int) -> None:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        cur = self.root
        cur.num_set.add(num)
        for i, w in enumerate(word):
            cur = cur.children[w]
            cur.depth = i + 1
            cur.num_set.add(num)

    def get_max_prefix_len(self, word: str) -> int:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                return cur.depth
            cur = cur.children[w]
            if len(cur.num_set) < 2:
                # NOTE: return depth of the parent, because there exist only the search word
                return cur.depth - 1
        return cur.depth


N = int(input())
S = []
trie = Trie()
for i in range(N):
    s = input()
    S.append(s)
    trie.insert(s, i)
ans = [trie.get_max_prefix_len(s) for s in S]
print(*ans, sep="\n")
