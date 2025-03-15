class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        if digits[l-1]!=9:
            digits[l-1]+=1
            return digits
        else:
            p=l-1
            while digits[p]==9:
                digits[p]=0
                p-=1
            if p==-1:
                digits.insert(0,1)
            else:
                digits[p]+=1
            return digits
            