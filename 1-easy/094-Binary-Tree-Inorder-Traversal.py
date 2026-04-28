# Problem: Binary Tree Inorder Traversal (LeetCode #94)
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Complexity: Time O(n), Space O(n) (recursion stack)
# Strategy: Recursive Depth-First Search (DFS) following the Inorder pattern: Left -> Root -> Right.

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    traversal = []

    def inOrder(root):
        if not root: return

        inOrder(root.left)
        traversal.append(root.val)
        inOrder(root.right)
    
    inOrder(root)
    return traversal