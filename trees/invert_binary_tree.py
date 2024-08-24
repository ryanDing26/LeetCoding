from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Level: Easy

        Problem Statement
        -----------------
        You are given the root of a binary tree root. Invert the binary tree
        and return its root.

        Approach
        --------
        1. If you are a valid node, swap the right and the left node, and then
           recursively call the invert method on the right and left children.
        2. At the end of this, return the node whose two children you swapped.
           You should eventually return the actual root at the very end.
           
        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        if root:
            # Could also do: root.left, root.right = root.right, root.left
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.right)
            self.invertTree(root.left)
            return root
