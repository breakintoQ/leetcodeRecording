class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n   #用这里使用循环
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_cost > sum_of_gas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += 1  #这个太大了会超时。
                # 这里如果改成i+=cnt+1 可以减少遍历次数，即从不行的那个开始往后算，因为中间的一定都不行
        return -1
