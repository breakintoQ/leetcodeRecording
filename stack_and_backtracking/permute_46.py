class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = [False]*len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True

                    backtrack()

                    path.pop()
                    used[i] = False

        backtrack()
        return result