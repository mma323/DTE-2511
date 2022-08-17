class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False
    
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            current.parent = parent
            while current != None:
                if e < current.element:
                    parent = current
                    current.left.parent = parent
                    current = current.left
                elif e > current.element:
                    parent = current
                    current.right.parent = parent
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
                parent.left.parent = parent
            else:
                parent.right = self.createNewNode(e)
                parent.right.parent = parent

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        current.parent = parent
        while current != None:
            if e < current.element:
                parent = current
                current.left.parent = parent
                current = current.left
            elif e > current.element: 
                parent = current
                current.right.parent = parent
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
                self.root.parent = None
            else:
                if e < parent.element:
                    parent.left = current.right
                    parent.left.parent = parent
                else:
                    parent.right = current.right
                    parent.right.parent = parent

        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left   
          

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

    def getNode(self, element):
        return self.getNodeHelper(self.root, element)

    def getNodeHelper(self, root, element):
        if root != None:
            if root == element:
                return(root)
            self.getNodeHelper(root.left)
            self.getNodeHelper(root.right)

    def isLeaf(self, element):
        return self.isLeafHelper(self.root, element)

    def isLeafHelper(self, root, element):
        if element.left == None and element.right == None:
            return True
        self.isLeafHelper(root.left)
        self.isLeafHelper(root.right)

    def getPath(self):
        path = []


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.parent = None
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None

numbers = [2, 4, 3, 1, 8, 5, 6, 7]
intTree = BST()
for e in numbers:
    intTree.insert(e)

intTree.delete(2)

for e in numbers:
    if intTree.isLeaf(e):
        print(intTree.getPath(e))