class Solution:
    def maxDepth(self, root) ->int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

# 深搜。基础深搜。今天没动脑子直接复制的，学习方法，都忘了已经
# 今天结束了，过生日奖励自己歇逼（
# 明天把树相关仔细看看