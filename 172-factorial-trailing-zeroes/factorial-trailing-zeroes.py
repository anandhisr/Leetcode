class Solution:
    def trailingZeroes(self, n: int) -> int:
        import math
        import sys
        sys.set_int_max_str_digits(0)
        
        dict={}
        dict1={}
        
        fact=math.factorial(n)
        s=str(fact)
        flag=False
        cnt=0
        for num in reversed(range(len(s))) : 
            if (s[num]=="0"):
                dict[num]=int(s[num])
        for i in dict.keys():
            if i == len(s)-1 and dict[i]==0:
                cnt+=1
                dict1[i]=0
                continue
            if dict[i]==0 and i+1 in dict1.keys():
                cnt+=1
                dict1[i]=0
        return cnt