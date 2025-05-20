class TreeNode:

    def __init__(self, parent, left, right, value):
        self.value = value
        self.parent = parent
        self.left_child = left
        self.right_child = right
    
    def is_external(self)-> bool:
        return self.left_child is None and self.right_child is None
    
    def is_internal(self)-> bool:
        return not self.is_external()
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()
    
    def node_height(self):
        #Base Case
        if self.is_external():
            return 0
        else:
            left_height = 0
            right_height = 0
            if self.left_child is not None:
                left_height = self.left_child.node_height()
            if self.right_child is not None:
                right_height = self.right_child.node_height()
            return max(left_height, right_height) + 1
    
class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.root is None
    
    def tree_height(self):
        return self.root.node_height()
    
    def add_root(self, value):
        if not self.root is None:
            raise ValueError("BinaryTree.add_root: root already exists")
        self.root = TreeNode(None, None, None, value)
        self.size += 1
        return self.root
    
    def add_right_child(self, parent, value):
        if not parent.right_child is None:
            raise ValueError("BinaryTree.add_right: right child already exists")
        parent.right_child = TreeNode(parent,None,None,value)
        self.size += 1
        return parent.right_child
    
    def add_left_child(self, parent, value):
         if not parent.left_child is None:
            raise ValueError("BinaryTree.add_left: left child already exists")
         parent.left_child = TreeNode(parent,None,None,value)
         self.size += 1
         return parent.left_child
    
    def print_tree(self, node=None, level = 0):
        if level == 0:
            node = self.root
        if node != None:
            self.print_tree(node.left_child, level + 1)
            print(" "*4*level + '->'+str(node))
            self.print_tree(node.right_child, level + 1)
        return
    
    def ancestors(self, node):
        pass