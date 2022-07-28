from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("a")
    print(trie.search("a"))
    print(trie.startsWith("a"))
