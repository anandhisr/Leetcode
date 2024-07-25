class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict={}
        cnt=0
        ocnt=0
        ochars=0
        if len(s)==1: return(1)
        for i in s:
            if i not in dict.keys():
                dict[i]=1
            else:
                dict[i]+=1
        print(dict)
        if (len(dict)==1): return(len(s))
        for i in dict.keys():
            if dict[i]%2==0:
                cnt+=dict[i]
            else:
                ocnt+=dict[i]
                ochars+=1
        if ocnt>0 : ocnt-=ochars-1
        return(cnt+ocnt)