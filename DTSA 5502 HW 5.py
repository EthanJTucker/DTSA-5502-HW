class TreeNode:
    # Constructor for tree nodde
    def __init__(self, key, parent_node=None):
        self.key = key # set the key
        self.parent = parent_node # set the parent_node
        self.left = None # set the left child to None -- no left child to begin with
        self.right = None # set the right child to None - no right child to begin with.
        self.curSum = None # This will help with speeding up problem 2
    
    def is_root(self):
        return parent_node == None
    
    # Function: insert
    # insert a node with key `new_key` into the current tree.
    def insert(self, new_key):
        key = self.key 
        if new_key == key:
            print(f'Already inserted key {key}. Ignoring')
        elif new_key < key: # new_key must go into the left subtree
            if self.left == None: # no left child?
                new_node = TreeNode(new_key, self) # create one with self as parent
                self.left = new_node # set the left pointer
            else:
                self.left.insert(new_key) # recursively call insert on left subtree
        else:  # new_key must go into the right subtree.
            assert new_key > key
            if self.right == None: # no right child?
                new_node = TreeNode(new_key, self) # create one
                self.right = new_node
            else: 
                self.right.insert(new_key) # recusively call insert on right subtree.

# TODO: Implement the function depthWiseTraverse below
def depthWiseTraverse(root_node):
    # This function inputs the root node of the tree.
    # root_node is an instance of the TreeNode class provided to you above
    # See description and example above.
    # your code here
    FIFO = [root_node]
    result = []
    
    while(len(FIFO) > 0):
        current_node = FIFO[0]
        FIFO.pop(0)
        result.append(current_node.key)
        
        if current_node.left != None:
            FIFO.append(current_node.left)
        if current_node.right != None:
            FIFO.append(current_node.right)
    
    return(result)

###########################################################################################################################################################
def make_tree(insertion_list):
    assert len(insertion_list) > 0
    root_node = TreeNode(insertion_list[0])
    for elt in insertion_list[1:]:
        root_node.insert(elt)
    return root_node

print('-- Test 1 --')
# Same as the example above
tree1 = make_tree([11, 18, 15,  13, 21, 17, 4])
lst1 = depthWiseTraverse(tree1)
print(lst1)
assert lst1 == [11, 4, 18, 15, 21, 13, 17]

print('-- Test 2 --')

tree2 = make_tree([3, 1, 2, 4, 6, 7])
lst2 = depthWiseTraverse(tree2)
print(lst2)
assert lst2 == [3, 1, 4, 2, 6, 7]

print('-- Test 3 --')
tree3 = make_tree([7, 3, 1, 2, 4, 6, 15, 8, 11, 10, 9])
lst3 = depthWiseTraverse(tree3)
print(lst3)
assert lst3 == [7, 3, 15, 1, 4, 8, 2, 6, 11, 10, 9]

print('All tests passed: 15 points')
###########################################################################################################################################################
def sumOfBranches(root_node):
    # return a list of sums 
    # your code here
    result = []
    root_node.curSum = root_node.key
    
    if root_node.left == None and root_node.right == None:
        result.append(root_node.key)
        return(result)
    
    if root_node.left != None:
        sumOfBranchesHelper(root_node.left, result)
    if root_node.right != None:
        sumOfBranchesHelper(root_node.right, result)
        

        
    return(result)
    
    
def sumOfBranchesHelper(node, result):
    node.curSum = node.key + node.parent.curSum
    if node.left == None and node.right == None:
        result.append(node.curSum)
        return
    else:
        if node.left != None:
            sumOfBranchesHelper(node.left, result)
        if node.right != None:
            sumOfBranchesHelper(node.right, result)


###########################################################################################################################################################
def make_tree(insertion_list):
    assert len(insertion_list) > 0
    root_node = TreeNode(insertion_list[0])
    for elt in insertion_list[1:]:
        root_node.insert(elt)
    return root_node

print('-- Test 1 --')
# Same as the example from problem 1
tree1 = make_tree([11, 18, 15,  13, 21, 17, 4])
lst1 = sumOfBranches(tree1)
print(lst1)
assert lst1 == [15, 57, 61, 50]

print('-- Test 2 --')
# Same as example from problem 2

tree2 = make_tree([11,4, 18, -1, 7, 15, 21, 2, 13, 17])
lst2 = sumOfBranches(tree2)
print(lst2)
assert lst2 == [16, 22, 57, 61, 50]

print('-- Test 3 --')
tree3 = make_tree([15])
lst3 = sumOfBranches(tree3)
print(lst3)
assert lst3 == [15]

print('-- Test 4 --')
tree4 = make_tree([4, 1, 2, 3, 8, 5, 6, 7,  10, 9])
lst4 = sumOfBranches(tree4)
print(lst4)
assert lst4 == [10, 30, 31]

print('All tests passed: 15 points!')
###########################################################################################################################################################

from math import sqrt

# You may use this function to test if a point lies inside given circle.
def ptInCircle(x,y, circles_list):
    for (xc,yc,rc) in circles_list:
        d = sqrt ( (x-xc)**2 + (y-yc)**2)
        if d <= rc:
            return True
    return False

def adjacent_node_locations(node):
    adjacent_nodes = []
    ## East Node
    if node.x - 1 >= 0:
        adjacent_nodes.append((node.x - 1, node.y))
    ## West Node
    if node.x + 1 <= node.width:
        adjacent_nodes.append((node.x + 1, node.y))
    ## South Node
    if node.y - 1 >= 0:
        adjacent_nodes.append((node.x, node.y - 1))
    ## North Node
    if node.y + 1 <= node.height:
        adjacent_nodes.append((node.x, node.y + 1))
        
    return(adjacent_nodes)

def relax(parent, child):
    if child.isAccessible() and child.d > parent.d + 1:
        child.pi = parent
        child.d = parent.d + 1
        
        
        
## I'm using the vertex data structure supplied in programming assignment 4 with
## a few modifications, as the rules said we were allowed to use course resources.
    
class Vertex: # This is the outline for a vertex data structure
    
    def __init__ (self,  x, y, forbidden_circles_list, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.d = float('inf') # the shortest path estimate
        self.processed = False # Has this vertex's final shortest path distance been computed
        # this is important for Dijksatra's algorithm
        self.pi = None # the parent vertex in the shortest path tree.
        self.adjacent_node_locations = adjacent_node_locations(self)
        self.forbidden_circles_list = forbidden_circles_list
        
    def isAccessible(self):
        return False == ptInCircle(self.x, self.y, self.forbidden_circles_list)
        

## This class will allow us to avoid creating duplicate copies of verticies
class Graph:
    def __init__(self, height, width):
        self.locations = [(i,j) for i in range(width + 1) for j in range(height + 1)]
        self.vert_list = [None] * len(self.locations)
    
    def vertexFromCoords(self, x, y):
        k = self.locations.index((x,y))
        return self.vert_list[k]
    
    def insertVertex(self, x, y, vert):
        k = self.locations.index((x,y))
        self.vert_list[k] = vert
    
    
## Will try modified BFS

def findPath(width, height, forbidden_circles_list):
    # width is a positive number
    # height is a positive number
    # forbidden_circles_list is a list of triples [(x1, y1, r1),..., (xk, yk, rk)]
    assert width >= 1
    assert height >= 1
    assert all(x <= width and x >=0 and y <= height and y >= 0 and r > 0 for (x,y,r) in forbidden_circles_list)
    # your code here
    
    
    graph = Graph(height, width)
    source = Vertex(0, 0, forbidden_circles_list, height, width)
    source.d = 0
    FIFO = [source]
    
    while len(FIFO) > 0:
        currentNode = FIFO[0]
        FIFO.pop(0)
        for adjacent_coords in currentNode.adjacent_node_locations:
            
            if graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]) != None:
                initialD = graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]).d
                relax(currentNode, graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]))
                finalD = graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]).d
                
                if finalD < initialD:
                    FIFO.append(graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]))
            
            else:
                graph.insertVertex(adjacent_coords[0], adjacent_coords[1], Vertex(adjacent_coords[0], adjacent_coords[1], forbidden_circles_list, height, width))
                relax(currentNode, graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]))
                
                if graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]).d != float('inf'):
                    FIFO.append(graph.vertexFromCoords(adjacent_coords[0], adjacent_coords[1]))
    
    path = list()
    
    if graph.vertexFromCoords(width, height) == None:
        return path
        
    else:
        currentNode = graph.vertexFromCoords(width, height)
        while currentNode != graph.vertexFromCoords(0,0):
            path.append((currentNode.x, currentNode.y))
            if (currentNode.x, currentNode.y) != (0,0):
                currentNode = currentNode.pi
            else:
                break
        
        path.reverse()
        return path
    
    
###########################################################################################################################################################
    
def checkPath(width, height, circles, path):
    assert path[0] == (0,0), 'Path must begin at (0,0)'
    assert path[-1] == (width, height), f'Path must end at {(width, height)}'
    (cur_x, cur_y) = path[0]
    for (new_x, new_y) in path[1:]:
        dx = new_x - cur_x
        dy = new_y - cur_y
        assert (dx,dy) in [(1,0),(-1,0), (0,1),(0,-1)]
        assert 0 <= new_x and new_x <= width
        assert 0 <= new_y and new_y <= height
        assert not ptInCircle(new_x, new_y, circles)
        cur_x, cur_y = new_x, new_y
    return
print('-- Test 1 -- ')

circles = [(2,2,0.5), (1,2,1)]
p = findPath(3, 3, circles)
print(p)
checkPath(3, 3, circles, p)
print('-- Test 2 -- ')

circles1 = [(2,2,1), (1,2,1)]
p1 = findPath(3, 3, circles1)
print(p1)
assert p1 == [], 'Answer does not match with ours'

print('-- Test 3 -- ')
p2 = findPath(5,5, circles1)
print(p2)
checkPath(5, 5, circles1, p2)

print('-- Test 4 --')

circles3 = [(1,2,0.5), (2,2,1), (3,3,1),(4,3,1)]
p3 = findPath(5, 5, circles3)
print(p3)
checkPath(5, 5, circles3, p3)

print('-- Test 5 --')
circles5 = [ (4,1, 1), (4,4,1),(2,6,1)]
p5 = findPath(6,6,circles5)
print(p5)
assert p5 == []
print('All tests passed: 15 points!')