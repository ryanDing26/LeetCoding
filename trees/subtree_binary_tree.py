from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given the roots of two binary trees root and subRoot, return true if
        there is a subtree of root with the same structure and node values of
        subRoot and false otherwise.

        A subtree of a binary tree tree is a tree that consists of a node in
        tree and all of this node's descendants. The tree tree could also be
        considered as a subtree of itself.

        Approach
        --------
        1. Do basic condition checking; if there is no subRoot, that means
           everything is a subtree. If there is no root, that means nothing is
           a subtree.
        2. Create a function to check if two trees are the exact same, and then
           call that and return True if that method returns True.
        2a. The function to check if two trees are the same should first check
            if the current root and subRoot are not NoneTypes. If they both
            are, that means you have consecutively hit the bottom of both the
            main and subtree at the same time, meaning that the subtree is a
            subtree. If both the root and subRoot actually exist, and their
            values match up, compare their rights and left childs to see if 
            they match up as well. Any other case would lead to subRoot not
            being a subtree, so we return False.
        3. If the same-tree method returns False, call the subtree method
           (the one we start with), to check if either the right or left child
           of the main tree matches up to be a subTree, recursively doing the
           process again.
           
        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        # No subtree == always a subtree
        if not subRoot:
            return True

        # No root = always no subtree
        if not root:
            return False

        return True if self.sameTree(root, subRoot) else self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Hit the bottom of the tree
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        # root.val != subRoot.val
        return False
        
