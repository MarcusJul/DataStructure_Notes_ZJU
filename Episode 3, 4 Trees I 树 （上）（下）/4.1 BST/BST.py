# BST 
class BSTnode(object):
    def __init__(self, data):
        self.data = data
        self.right, self.left = None, None
        self.flag = 0
      
class BST(object):
    def __init__(self, data):
        self.root = self.MakeTree()
        self.right, self.left, self.flag = self.root.right, self.root.left(), self.root.flag
        
    def MakeTree(self, data):
        return BSTnode(data)
    
    def Insert(self, data):
        if self.root!=None:
            node = BSTnode(data)
            if node.data < self.root.data:
                self.root.left.Insert(data)
            else:
                self.root.right.Insert(data)
        else:
            return self.root

    def Reset(self, root):
        if root.left:
            Reset(root.left)
        if root.right:
            Reset(root.right)
        root.flag = 0
                
            
        
        