from random import randint
import time
import re
import sys

sys.setrecursionlimit(50000)

class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.parent = None

    def is_external(self):
        return self.left is None and self.right is None
    
    def is_internal(self):
        return  not self.is_external()
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self)
    

class TreeSet:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def _add_helper(self, root, value):
        if root is None:
            self.size += 1
            return TreeNode(value)
        elif value < root.value:
            root.left = self._add_helper(root.left, value)
            root.left.parent = root
        elif value > root.value:
            root.right = self._add_helper(root.right, value)
            root.right.parent = root

        return root
    
    def add(self, v)->None:
        self.root = self._add_helper(self.root, v)

    def _discard_helper(self, root, value):
        if root is None:
            return None
        if value < root.value:
            root.left = self._discard_helper(root.left, value)
            if root.left is not None:
                root.left.parent = root
        elif value > root.value:
            root.right = self._discard_helper(root.right, value)
            if root.right is not None:
                root.right.parent = root
        else:
            #Case 01: Node is leaf
            if root.is_external():
                size -= 1
                return None
            #case 02: Node has one child
            if root.left is None:
                self.size -= 1
                return root.right
            if root.right is None:
                self.size -= 1
                return root.left
            #case 03: Node has two children
            pred = root.left
            while pred.right is not None:
                pred = pred.right

            root.value = pred.value
            root.left = self._discard_helper(root.left, pred.value)
        return root

    def discard(self, v)->None:
        self._discard_helper(self.root, v)

    #LAB
    def contains(self, v)->bool:
        current = self.root
        while current is not None:
            if v < current.value:
                current = current.left
            elif v > current.value:
                current = current.right
            else:
                return True
        return False

    def union(self, other):
        pass

    def intersection(self, other):
        pass

    def difference(self, other):
        pass

    #LAB
    def min(self):
        if self.is_empty():
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value
    #LAB
    def max(self):
        if self.is_empty():
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def _recursive_str(self, r, level):
        # base case: tree is empty, return empty string
        if r is None:
            return ""
        return level*"  " + str(r) +"\n"+ self._recursive_str(r.left, level+1) +\
              self._recursive_str(r.right, level+1)
    
    def __str__(self):
        return self._recursive_str(self.root, 0)

def _main():
    nederlands_tree = TreeSet()
    les_miserables_tree = TreeSet()
    
    start_time = time.time()
    with open('nederlands_short.txt', 'r') as f:
        for line in f:
            word = line.strip().lower()
            if word:
                nederlands_tree.add(word)
    nederlands_time = time.time() - start_time
    
    start_time = time.time()
    with open('LesMiserables.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        words = re.findall(r'\b[a-zA-Z]+\b', content.lower())
        for word in words:
            les_miserables_tree.add(word)
    les_miserables_time = time.time() - start_time
    
    print(f"Nederlands tree build time: {nederlands_time:.4f} seconds")
    print(f"Les Miserables tree build time: {les_miserables_time:.4f} seconds")
    print(f"Nederlands tree size: {nederlands_tree.get_size()}")
    print(f"Les Miserables tree size: {les_miserables_tree.get_size()}")

if __name__ == "__main__":
    _main()