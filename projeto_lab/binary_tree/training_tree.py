#criando uma árvore binária


class tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = tree_node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print(' ', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(' ',end='')


if __name__ == "__main__":
    # tree = BinaryTree(1)
    # tree.root.right = tree_node(2)
    # tree.root.left = tree_node(3)

    # print(tree.root)
    # print(tree.root.right)
    # print(tree.root.left)

    tree = BinaryTree()
    n1 = tree_node('1')
    n2 = tree_node('2')
    n3 = tree_node('3')
    n4 = tree_node('4')
    n5 = tree_node('5')
    n6 = tree_node('6')
    n7 = tree_node('7')
    n8 = tree_node('8')
    n9 = tree_node('9')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n3

    tree.simetric_traversal()
    print()