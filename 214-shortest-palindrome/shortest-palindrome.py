class Solution:
    def shortestPalindrome(self, s: str) -> str:

        s1=""
        txt = ""
        if len(s)==1 or (s==s[::-1]): return s
        for i in reversed(s):
            s1+=i
            txt=s1+s
            if (txt==txt[::-1]):
                print(txt,"palindrome")
                break
        return(txt)