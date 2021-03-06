from Queue import Queue, Stack

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
        elif traversal_type == 'levelorder':
            return self.levelorder_print(tree.root)
        elif traversal_type == 'reverse_levelorder':
            return self.reverse_levelorder_print(tree.root)
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

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ''
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + '-'
        return traversal

    def height(self,node):

        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size
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

# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
print('******')
print(tree.height(tree.root))
print('tree size ---', tree.size())

print("preorder--",tree.print_tree('preorder'))
print("inorder----",tree.print_tree('inorder'))
print("postorder-----",tree.print_tree('postorder'))
print("levelorder-----",tree.print_tree('levelorder'))
print("reverse_levelorder-----",tree.print_tree('reverse_levelorder'))






