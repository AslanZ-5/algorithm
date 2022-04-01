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
            return self.preorder_print(tree.root, "")
        if traversal_type == 'inorder':
            return self.print_inorder(tree.root, "")
        if traversal_type == 'postorder':
            return self.print_postorder(tree.root, "")
        else:
            print(f"Travelsal type unsupported")

    def preorder_print(self, start, traversal):
        """Root => Left => Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def print_inorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.print_inorder(start.right, traversal)
        return traversal

    def print_postorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal = self.print_inorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print('preorder',tree.print_tree('preorder'))
print('inorder',tree.print_tree('inorder'))
print('postorder',tree.print_tree('postorder'))