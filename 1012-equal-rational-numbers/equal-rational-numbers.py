class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        l=[]
        l1=[]
        s1=""
        t1=""
        f1=False
        f2=False
        cnt=0
        for i in s:
            if i!="(" and i!=")":
                cnt+=1
        if cnt==len(s):
            f1=True
            s1=s
        cnt=0
        for i in t:
            if i!="(" and i!=")":
                cnt+=1
        if cnt==len(t):
            f2=True 
            t1=t
        in_brackets=False
        current_substring=""
        if f1!=True:
            for c in s:
                if c == "(":
                    in_brackets = True
                elif c == ")" and in_brackets:
                    l.append(current_substring)
                    current_substring = ""
                    in_brackets = False
                elif in_brackets:
                    current_substring += c
            
            if current_substring:
                l.append(current_substring)
            if len(l)>0:
                if l[0] in s:
                    s1=s.replace("("+l[0]+")",'')
                print(s1)
        in_brackets=False
        if f2!=True:
            for c in t:
                if c == "(":
                    in_brackets = True
                elif c == ")" and in_brackets:
                    l1.append(current_substring)
                    current_substring = ""
                    in_brackets = False
                elif in_brackets:
                    current_substring += c
            if len(l1)>0:
                if l1[0] in t:
                    t1=t.replace("("+l1[0]+")",'')
                print(t1)
        
        for i in range(10):
            if len(l)>0 and f1!=True:
                s1+=l[0]
            if len(l1)>0 and f2!=True:
                t1+=l1[0]
        if (len(s1)>0 and len(t1)>0):    
            if abs(float(s1)-float(t1))<0.000000001:
                return(True)
        return False
        