class Trie:

    def __init__(self, val: int = None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.count = 0
        self.children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = Trie(c)
                
            cur = cur.children[c]
            
            if i == len(word) - 1:
                cur.count += 1
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        i = 0
        while i < len(word) and word[i] in cur.children:
            cur = cur.children[word[i]]
            i += 1
            
        return i == len(word) and cur.count >= 1
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self
        i = 0
        while i < len(prefix) and prefix[i] in cur.children:
            cur = cur.children[prefix[i]]
            i += 1
            
        return i == len(prefix)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)