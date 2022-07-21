from collections import defaultdict


class Trie:

    def __init__(self):
        self.edge = defaultdict(set)
        self.words = set()

    def insert(self, word: str) -> None:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        for i in range(len(word)-1):
            self.edge[(i, word[i])].add((i+1, word[i+1]))
        self.words.add(word)

    def search(self, word: str) -> bool:
        """
        Time complexity : O(1)
        Space complexity : O(1)
        """
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        if self.search(prefix):
            return True
        for i in range(len(prefix)):
            if (i, prefix[i]) not in self.edge or (i+1 < len(prefix) and (i+1, prefix[i+1]) not in self.edge[(i, prefix[i])]):
                return False
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("a")
    print(trie.search("a"))
    print(trie.startsWith("a"))
