


from python.projeto_lab.lab_tree import BinaryTree


if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node ('1')
    n2 = Node ('2')
    n3 = Node ('3')
    n4 = Node ('4')
    n5 = Node ('5')
    n6 = Node ('6')
    n7 = Node ('7')
    n8 = Node ('8')
    n9 = Node ('9')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2

