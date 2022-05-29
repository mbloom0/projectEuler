#Problem 18: Maximum path sum I
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
   3
  7 4
 2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
"""
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
#Plan: modified binary search tree, go down route with biggest numbers

triangle =                  ["75",
                           "95 64",
                         "17 47 82",
                       "18 35 87 10",
                      "20 04 82 47 65",
                    "19 01 23 75 03 34",
                  "88 02 77 73 07 63 67",
                 "99 65 04 28 06 16 70 92",
               "41 41 26 56 83 40 80 70 33",
              "41 48 72 33 47 32 37 16 94 29",
            "53 71 44 65 25 43 91 52 97 51 14",
          "70 11 33 28 77 73 17 78 39 68 17 57",
         "91 71 52 38 17 14 91 43 58 50 27 29 48",
       "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
     "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]

#tiny test triangle
#triangle =   ["3",
#             "7 4",
#            "2 4 6",
#           "8 5 9 3"]


triangleList = [list(map(int,x.split(" "))) for x in triangle]
print(triangleList)

    # paths = []
    # pathTriangle = [list(map((lambda x:0),y)) for y in triangleList]
    # numLayers = len(triangleList)-1
    # width = len(triangleList[numLayers])

    # print( list(range(numLayers,-1,-1)))
    # for layer in range(numLayers,-1,-1):
    #     for i in range(width -numLayers-layer -1):
    #         # if i == width -numLayers-layer:
    #         #     continue
    #         if triangleList[layer][i] < triangleList[layer][i+1]:
    #             pathTriangle.copy()[layer][i+1] += 1
    #         else:
    #             pathTriangle.copy()[layer][i] += 1

    #         print(triangleList[layer][i])



#could fix this usign a dictionary instead of locla variables in custom data type
# """ class BinaryPathTree:
#     def __init__(self, root):
#         self.root = root """

# def numberOfChildren(node):
#     num = 0
#     if node.hasLeftChild():
#         num =+ numberOfChildren(node.getLeftChild())
#     elif node.hasRightChild():
#         num =+ numberOfChildren(node.getRightChild())
#     return num

class Node:
    """not a regular binary search tree, the nodes are connected like described above"""
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None
    
    def hasLeftChild(self):
        return self.leftChild != None
    
    def hasRightChild(self):
        return self.rightChild != None

    def hasParent(self):
        return self.parent != None
    
    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getParent(self):
        return self.parent

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild
        if self.leftChild != None:
            self.leftChild.parent = self
            pass
    
    def setRightChild(self, rightChild):
        self.rightChild = rightChild
        if self.rightChild != None:
            self.rightChild.parent = self
            pass
    
#create tree structure using Nodes from trianglelist
root = Node(triangleList[0][0])

def listToTree(triangleList, currNode):
    """recursively build tree in current order without sorting from triangleList, creating a left and right sub triangle to recurse on each time"""
    leftTriangle = list(map((lambda lst: lst[:len(lst)-1]),triangleList[1:]))
    rightTriangle = list(map((lambda lst: lst[1:]),triangleList[1:]))
    if len(triangleList) == 1:
        #no more layers below
        return 
    if len(triangleList[0]) == 1:
        currNode.setLeftChild(Node(leftTriangle[0][0]))
        listToTree(leftTriangle, currNode.getLeftChild())
        currNode.setRightChild(Node(rightTriangle[0][0]))
        listToTree(rightTriangle, currNode.getRightChild())

    
def pathGen(triangleList, currNode):
    """recursively generate paths from root to leafs"""
    nextTriangleList = triangleList[1:]
    if len(triangleList) == 1:
        return currNode.data
    #if len(triangleList) == 2:
    #    return max(currNode.data + currNode.getLeftChild().data, currNode.data + currNode.getRightChild().data)
    #el
    if currNode.hasLeftChild() and currNode.hasRightChild():
        return max(currNode.data + pathGen(nextTriangleList, currNode.getLeftChild()), currNode.data + pathGen(nextTriangleList, currNode.getRightChild()))
    #elif currNode.hasLeftChild():
        return currNode.data + pathGen(nextTriangleList, currNode.getLeftChild())
    #elif currNode.hasRightChild():
        return currNode.data + pathGen(nextTriangleList, currNode.getRightChild())


def __main__():
    listToTree(triangleList, root)
    print(pathGen(triangleList, root))


listToTree(triangleList, root)
print(pathGen(triangleList, root))

#print(pathGen(triangleList))

#def insert(root, value):
#    """special insert that allows the right node of the node adjacent to a node to be the same as it's left node"""
#     #if binary search tree is empty, make a new node and declare it as root
#     if root is None:
#         root=BinaryTreeNode(value)
#         return root
#     #binary search tree is not empty, so we will insert it into the tree
#     #add from left to right, m
#     if root.leftChild == None:
#         root.leftChild = BinaryTreeNode(value)
#         root.numChildren += 1
#     elif root.rightChild == None:
#         root.rightChild = BinaryTreeNode(value)
#         root.numChildren += 1
#     else:
#         root.rightChild.leftChild = root.leftChild.rightChild
#         root.leftChild.rightChild = root.rightChild.leftChild
#         if root.leftChild.numChildren <= root.rightChild.numChildren: 
#             insert(root.leftChild, value)
#         else:
#             insert(root.rightChild, value)

#     return root


"""
print(triangleTree.data)
print(triangleTree.leftChild.data)
print(triangleTree.rightChild.data)
print(triangleTree.leftChild.leftChild.data)
print(triangleTree.leftChild.rightChild.data)
print(triangleTree.rightChild.leftChild.data)

print(triangleTree.rightChild.rightChild.data)
#last row
print(triangleTree.leftChild.leftChild.leftChild.data)
print(triangleTree.leftChild.leftChild.rightChild.data)
#would repeat here ift right then left at last two for last print
print(triangleTree.leftChild.rightChild.rightChild.data)
print(triangleTree.rightChild.rightChild.rightChild.data)
"""