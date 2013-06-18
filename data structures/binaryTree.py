__author__ = 'Michal'
import random, unittest

class BinarySearchTree():

    def __init__(self):
        #Sets up the root member
        self.root = None

    def insert(self, data):
        '''
            In place data insertion according to the rules of a BST
        '''
        newNode = Node(data)
        if self.root is None: #insertion
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

    def find(self, data):
        '''
            Attempts to find the node corresponding to the given data
        '''
        node = self.root
        while node is not None:
            # Did we find the node
            if node.data == data:
                return node
            else:
                # Look further down the tree
                if data < node.data:
                    node = node.left
                else:
                    node = node.right
        return node
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

'''
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse
'''
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
        #number of nodes to insert
        self.itemsToGen = 30
        #create the bst and insert in (itemsToGen) many nodes
        self.bst = BinarySearchTree()
        test = [i for i in range(self.itemsToGen)]
        random.shuffle(test)
        for num in test:
            self.bst.insert(num)

    def test_Node(self):
        #Ensure that the node contains the proper value and prints correctly.
        testNode = Node(self.randNodeVal)
        correct = str(self.randNodeVal)
        self.assertEqual(str(testNode), correct)

    def test_BinarySearchTree_insertion(self):
        #checks whether the insertion (and to extent in order traversal) is implemented correctly
        correct = [i for i in range(self.itemsToGen)]
        check = self.bst.traversal().split(',')
        answer = []
        for sNum in check:
            answer.append(int(sNum))
        self.assertEqual(answer,correct)

    def test_BinarySearchTree_find(self):
        for i in range(15):
            randElement = random.randint(0,self.itemsToGen -1)
            self.assertEqual(self.bst.find(randElement).data,randElement)





unittest.main()




if __name__ is '__main__':
    unittest.main()

