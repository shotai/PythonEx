class Node():
    def __init__(self, value):
        self.value = value  # Integer
        self.left = None
        self.right = None
        self.parent = None  # May or may not need it

    def __repr__(self):
        return '<class Node value=%d>' % self.value


class BinarySearchTree():
    def __init__(self, root):
        self.root = root

    def find_node(self, value):
        # Return Node if node found, otherwise return None
        def helper(node):
            if node.value == value:
                return node
            if not node:
                return 
            left = helper(node.left)
            if left:
                return left
            right = helper(node.right)
            if right:
                return right
        return helper(self.root)

    def delete_node(self, value):
        # Return True if node found and deleted, return False otherwise
        # Cannot increase the height of the tree
        
        deleted_node = self.find_node(value)
        
        if not deleted_node:
            return False
        if not deleted_node.parent:
            if deleted_node.left  :
                left =  deleted_node.left
                self.root.left = left.left
                self.root.right = left.right
                self.root.value = left.value
            if deleted_node.right :
                right =  deleted_node.right
                self.root.left = right.left
                self.root.right = right.right
                self.root.value = right.value
            return True
            
                
        
        # no children
        if not deleted_node.left and not deleted_node.right:
            if value> deleted_node.parent.value:
                deleted_node.parent.left = None
            else:
                deleted_node.parent.right = None
            return True
        # one children
        elif deleted_node.left and not deleted_node.right:
            tmp = deleted_node.left
            if deleted_node.parent.left is deleted_node:
                deleted_node.parent.left = tmp
                
            else:
                deleted_node.parent.right = tmp
        elif deleted_node.right  and not deleted_node.left:
            tmp = deleted_node.right
            if deleted_node.parent.left is deleted_node:
                deleted_node.parent.left = tmp
            else:
                deleted_node.parent.right = tmp
            return True
       
        elif deleted_node.right and deleted_node.left:
            # 2 children
            tmp = deleted_node
            right_child = deleted_node.right
            while right_child.left:
                tmp = right_child
                right_child = right_child.left
            
            tmp.value = right_child.value
            
            if tmp.left == right_child:
                tmp.left = right_child.right
            else:
                tmp.right = right_child.right
            return True
        
        
        return False

#  3
# 2
#1
# deleteNode(2)
# 3
#1

# 4
#3  5
#1 2
# tmp = 3
# right_child = 2


# 4
# 2  5
# 1 2

# tmp = 2
# tmp.left = 1
#else:
#  tmp.right = right_child.right
# tmp.right = None

# 4
# 2  5
# 1

# node = bst.findNode(3)
# assert node.value == 3
# bst.deleteNode(3)
# node.value == 2
# assert node.value == 3

root = Node(3)
left = Node(2)
right = Node(4)
left1 = Node(1)
left.parent = root
left.left = left1
left1.parent = left
right.parent = root
root.left = left
root.right = right

bst = BinarySearchTree(root)
print(bst.find_node(3))
print(bst.delete_node(2))
print(bst.root)
print(bst.root.left)
