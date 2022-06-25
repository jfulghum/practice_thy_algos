# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
# https://neetcode.io/
# https://www.youtube.com/watch?v=oobqoCJlHA0

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
