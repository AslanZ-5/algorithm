from . import Queue.Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, '')
        else:
            print('Traversal type ' + str(traversal_type) + ' is not supported')
            return False
    def inorder_print(self,start,traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right,traversal)
        return traversal
    def preorder_print(self,start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self,start,traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal = self.inorder_print(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal

#            1
#         /     \
#        2       3
#       /  \    /  \
#      4    5  6    7
#
#

# Set up tree:
tree = BinaryTree("F")
tree.root.left = Node("B")
tree.root.right = Node("G")
tree.root.left.left = Node("A")
tree.root.left.right = Node("D")
tree.root.left.right.left = Node("C")
tree.root.left.right.right = Node("E")
tree.root.right.right = Node("I")
tree.root.right.right.right = Node("H")
tree.root.right.right.right.left = Node("C")
tree.root.right.right.right.right = Node("X")


# tree.root.right.right.right = Node(8)

print("preorder--",tree.print_tree('preorder'))
print("inorder----",tree.print_tree('inorder'))
print("postorder-----",tree.print_tree('postorder'))






