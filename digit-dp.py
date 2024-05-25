from functools import cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low = [int(i) for i in str(low-1)]
        high = [int(i) for i in str(high)]
        if len(low) < len(high):
            low = [0] * (len(high) - len(low)) + low
        q = [low, high]
        n = len(high)
        @cache
        def dp(li,idx,rem,oddCount,evenCount,cap,taken):
            num = q[li]
            if idx == n:
                return rem == 0 and oddCount == evenCount and taken
            mx = 9
            if cap:
                mx = min(mx, num[idx])
            ans = 0
            for i in range(mx+1):
                nrem = (10*rem + i)%k
                ntaken = taken or i != 0
                noddcount = oddCount
                nevencount = evenCount
                if ntaken:
                    odd = i%2
                    noddcount+=odd
                    nevencount+=1-odd
                ncap = cap and i == num[idx]
                ans+=dp(li,idx+1,nrem,noddcount,nevencount,ncap,ntaken)
            return ans
        return dp(1,0,0,0,0,True,False) - dp(0,0,0,0,0,True,False)