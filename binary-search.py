class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)


# Verilen dizi
input_array = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# BST oluştur
root_node = None
for element in input_array:
    root_node = insert(root_node, element)

# BST'yi yazdır
print("Oluşturulan Binary Search Tree:")
print_tree(root_node)
