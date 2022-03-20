class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["-"] = True

    def search(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
