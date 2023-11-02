# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,ans,prev_val,cur_length):
        if not root:
            return
        # if current node value is 1 greater than the parent's value, update the result and recursively find answer for both left and right child    
        if root.val == prev_val+1:
            ans[0] = max(ans[0],cur_length+1)
            self.helper(root.left,ans,root.val,cur_length+1)
            self.helper(root.right,ans,root.val,cur_length+1)
        # else start new traversal with current length as 1 and prev value as current node's value
        else:
            self.helper(root.left,ans,root.val,1)
            self.helper(root.right,ans,root.val,1)
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = [1]
        if not root:
            return 0
        # call helper function with previous value as some non valid value as it's the first node
        self.helper(root,ans,-float('inf'),1)
        return ans[0]
        
