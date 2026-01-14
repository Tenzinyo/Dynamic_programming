class Node:
    def __init__(self) -> None:
        self.children = dict()
        self.is_end_word = False
class Trie:
    def __init__(self) -> None:
        self.root = Node()
    def insert(self,word):
        current_node = self.root()
        for c in word:
            if c in current_node.children:
                current_node.children[c] = Node()
            current_node = current_node.children[c]

        current_node.is_end_word = True  
        
    def search(self,word):
        current_node = self.root()
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.is_end_word
    def remove(self,word):
        self._delete(self.root,word,0)
        pass
    def has_prefix(self,prefix):
        current_node = self.root()
        for p in prefix:
            if p not in current_node.children:
                return False
            current_node = current_node.children[p]
        return True
                
                
    def starts_with(self, prefix):
        
        pass
    def list_words(prefix):
        pass
    
    def _delete(self,root,word,index):
        current_node = self.root()
        if index == len(word):
            if not current_node.is_end_word:
                 return False
            current_node.is_end_word = False
            return len(current_node.children) == 0
        c = word[index]
        node = current_node.children.get(c)
        if node is None:
            return False
        delete = self._delete(node,word,index+1)
        if delete:
            del current_node.children[c]
            return len(current_node.children) == 0 and not current_node.is_end_word
        return False
            
                  
        
    