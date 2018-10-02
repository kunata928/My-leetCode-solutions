"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return [] 
        res = []
        stack = []
        stack.append(root)
        while  stack:
            tmp = stack.pop()
            for child in tmp.children:
                stack.append(child)
            res.append(tmp.val)
        res.reverse()
        return res