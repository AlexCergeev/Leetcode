from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> List[int]:
    if root is None: return []

    def dfs(root, res):
        if root is None: return
        dfs(root.left, res)
        res.append(root.val)
        dfs(root.right, res)
        return res

    return dfs(root, [])



a = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
print(inorderTraversal(a))
