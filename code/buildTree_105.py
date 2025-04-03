# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # 1. 前序遍历的第一个元素是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. 在中序遍历中找到根节点的位置
        root_index = inorder.index(root_val)

        # 3. 划分左子树和右子树
        left_inorder = inorder[:root_index]  # 中序遍历的左子树
        right_inorder = inorder[root_index + 1:]  # 中序遍历的右子树

        #注意这里是因为，前序的特点是左边都遍历完了，剩下的是右边
        left_preorder = preorder[1:1 + len(left_inorder)]  # 前序遍历的左子树
        right_preorder = preorder[1 + len(left_inorder):]  # 前序遍历的右子树

        # 4. 递归构造左子树和右子树
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
            

    #这个没写出来，要看
    #还挺聪明，有意思