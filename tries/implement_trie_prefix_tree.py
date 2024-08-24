'''
Level: Medium

Problem Statement
-----------------
A prefix tree (also known as a trie) is a tree data structure used to
efficiently store and retrieve keys in a set of strings. Some applications of
this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

- PrefixTree():                      Initializes the prefix tree object.
- void insert(String word):          Inserts the string word into the prefix 
                                     tree.
- boolean search(String word):       Returns true if the string word is in the
                                     prefix tree (i.e., was inserted before),
                                     and false otherwise.
- boolean startsWith(String prefix): Returns true if there is a previously
                                     inserted string word that has the prefix
                                     prefix, and false otherwise.
Approach
--------
1. Implement a Node class that stores a given node's children and whether or
   not the node itself is a word node.
2. Set the root of the PrefixTree to just be a Node.
3. For insert, starting at the root, continue to traverse down and check if c
   is a child of the current node you are on. If it is not, then create it as a
   Node. Regardless, set the current node equal to that child, and after the
   operation, set the end/word status of the node you ended on to be True.
4. For search, perform the same operations that you did for insert, except when
   c is not a child of the current node you are on, return False. At the very
   end, return whether or not the node you end on is a end/word node with
   return self.end.
5. For startsWith, do the same thing as search, but instead of having to return
   whether the node you end on is a end/word node, simply return True.
   
TC/SC
-----
TC: insert: O(n), search: O(n), startsWith: O(n)
SC: O(n)
'''

class PrefixTreeNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixTreeNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        