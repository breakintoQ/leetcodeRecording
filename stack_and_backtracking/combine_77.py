class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []

        def backtrack(start_index):
            if len(path) == k:
                result.append(path[:])
                return 
            
            for i in range(start_index, n-(k-len(path))+2):
                path.append(i)
                backtrack(i+1)
                path.pop()

        
        backtrack(1)
        return result