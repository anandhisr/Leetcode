class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        s1=""
        for i in s.split():
            l.append(i)
        print(l)
        for i in reversed(l):
            s1+=i+" "
        return(s1.rstrip())