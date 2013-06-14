__author__ = 'Michal'
import random, unittest

class BinarySearchTree():

    def __init__(self):
        #Sets up the root member
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None: #insertition
            #This node in the tree is empty
            self.root = newNode
        else: #tree traversal
            node = self.root
            #traverse through the tree and find the insertion point
            while True:
                #check whether to travel the left or right side
                if data <= node.data:
                    if node.left is None:
                        node.left = newNode
                        break
                    node = node.left
                else :
                    if node.right is None:
                        node.right = newNode
                        break
                    node = node.right
        return newNode

    def traversal(self):

        def inOrderTraversal(node):
            '''
            In-order (symmetric):
                Traverse the left subtree.
                Visit the root.
                Traverse the right subtree.
                    Ref: Wikipedia
            '''
            output = ''
            if node is None:
                return ''
            else :
                output += inOrderTraversal(node.left)
                output += str(node) + ','
                output += inOrderTraversal(node.right)
            return output
        return inOrderTraversal(self.root)[:-1]

class Node:
    left, right, data = None, None, 0

    def __init__(self, data):
        #set the data member field
        self.data = data

    def __str__(self):
        # outputs the node
        return str(self.data)

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.randNodeVal = random.randint

    def test_Node(self):
        #Ensure that the node contains the proper value and prints correctly.
        testNode = Node(self.randNodeVal)
        correct = str(self.randNodeVal)
        self.assertEqual(correct, str(testNode))

    def test_BineraySearchTree_insertation(self):
        #checks whether the insertion (and to extent in order traversal) is implemented correctly
        itemsToGen = 30
        bst = BinarySearchTree()
        correct = [i for i in range(itemsToGen)]
        test = [i for i in range(itemsToGen)]
        random.shuffle(test)
        for num in test:
            bst.insert(num)
        check = bst.traversal().split(',')
        answer = []
        for sNum in check:
            answer.append(int(sNum))
        self.assertEqual(answer,correct)





unittest.main()




if __name__ is '__main__':
    unittest.main()

