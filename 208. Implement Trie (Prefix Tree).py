class PrefixNode:
    def __init__(self):
        self.nodes = {}
        self.last_latter = False


class PrefixTree:
    def __init__(self):
        self.node = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.node
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = PrefixNode()
            curr = curr.nodes[c]
        curr.last_latter = True

    def search(self, word: str) -> bool:
        curr = self.node
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.last_latter

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for c in prefix:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True
