class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None  # smaller than the current node
        self.right = None  # larger than the current node


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_recursive(self.root, new_val)

    def insert_recursive(self, current, new_val):
        if new_val > current.value:
            if current.right:
                self.insert_recursive(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_recursive(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_recursive(self.root, find_val)

    def search_recursive(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif find_val > current.value:
                return self.search_recursive(current.right, find_val)
            else:
                return self.search_recursive(current.left, find_val)
        else:
            return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
