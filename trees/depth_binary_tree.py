from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given the root of a binary tree, return its depth.

        The depth of a binary tree is defined as the number of nodes along the
        longest path from the root node down to the farthest leaf node.
        
        Approach
        --------
        1. If the node you are at is NoneType, return 0.
        2. If not, add 1 to the depth whilst recursively calling maxDepth on
           the right and left children node of your current node.

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))