class Solution:

    def addBinary(self, a: str, b: str) -> str:
        def btd(s: str) ->int:
            l= len(s)
            ans = 0
            for i in range(0,l,1):
                if s[i]=='1':
                    ans+=2**(l-i-1)
            return ans
        
        def dtb(n: int) ->str:
            if n == 0:
                return '0'
            s = ''
            while n>0:
                s= str(n%2)+s
                n = n//2
            return s

        a_d = btd(a)
        b_d = btd(b)
        ans = a_d+b_d
        return dtb(ans)







#十进制转二进制应该有库，但是我不知道是啥，先自己写一个
#直接用库需要一行： return bin(int(a,2)+int(b,2))[2:]