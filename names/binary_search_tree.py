"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
    on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
    on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # ? is tree empty?
        # * yes
        if self.value is None:
            # make a new node
            self.value = BSTNode(value)
        # * no
        else:
            # * insert left (value is less than current/self)
            if value < self.value:
                if self.left is not None:
                    self.left.insert(value)
                # if left is empty, start new node
                else:
                    self.left = BSTNode(value)
            # * insert right (value is more than current/self)
            else:
                if self.right is not None:
                    self.right.insert(value)
                # if right is empty, start new node
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # ? is current value = target?
        if self.value is target:
            return True
        else:
            # * goes left
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                #  * goes right
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return
        
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if not self.value:
            return
        else:
            fn(self.value)
            # runs for each on left 
            if self.left:
                self.left.for_each(fn)
            #  runs for each on right
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # * read tree left to right and order 1-10
        # * if not empty, print left of node, then node value, then right of node - due to rules of left < value
        if node:
            # First recur on left child 
            self.in_order_print(node.left)
            # then print the data of node 
            print(node.value)
            # now recur on right child 
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # * pyramid, queue
        if self.value is None:
            return

        queue = []

        queue.append(node)

        while(len(queue) > 0):
            print(queue[0].value)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # * all the way down "branch", stack
        if self.value == None:
            return
        
        stack = []

        stack.append(node)

        while(len(stack) > 0):
            node = stack.pop()
            print(node.value)

            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Preorder(tree)
        # 1. Visit the root.
        # 2. Traverse the left subtree, i.e., call Preorder(left-subtree)
        # 3. Traverse the right subtree, i.e., call Preorder(right-subtree)
        if node:
            # First print the data of node 
            print(node.value)
            # then recur on left child 
            self.pre_order_dft(node.left)
            # now recur on right child 
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
    #    Postorder(tree)
    #    1. Traverse the left subtree, i.e., call Postorder(left-subtree)
    #    2. Traverse the right subtree, i.e., call Postorder(right-subtree)
    #    3. Visit the root.
        if node:
            # First recur on left child 
            self.post_order_dft(node.left)
            # now recur on right child 
            self.post_order_dft(node.right)
            # then print the data of node 
            print(node.value)

