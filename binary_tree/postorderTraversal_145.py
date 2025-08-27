# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#后序，递归
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root):
            if root:
                if root.left:
                    dfs(root.left)

                if root.right:
                    dfs(root.right)
                
                result.append(root.val)
        
        dfs(root)
        return result

# 或者，添加到尾部然后整体反转（直接根右左然后翻转）
def postorderTraversal_reversed_v2(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    result_temp = []
    stack = [root]

    while stack:
        node = stack.pop()
        result_temp.append(node.val)  #或者这里用result.insert（0，val）
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result_temp[::-1]


#更复杂但标准的后序：
def postorderTraversal_prev(root: TreeNode) -> List[int]:
    if not root:
        return []
        
    result = []
    stack = []
    current = root
    prev = None  # 记录上一个访问的节点

    while current or stack:
        # 1. 一路向左
        while current:
            stack.append(current)
            current = current.left
        
        # 2. 查看栈顶元素
        node = stack[-1] # peek
        
        # 3. 判断右子树是否为空或已访问
        if not node.right or node.right == prev:
            # 如果是，则可以访问当前节点
            node = stack.pop()
            result.append(node.val)
            prev = node
            # current 设为 None，这样下一轮循环会继续从栈中取元素
            current = None 
        else:
            # 否则，转向右子树
            current = node.right

    return result