class Solution:
    def decodeString(self, s: str) -> str:
        import re        
        l=[]
        s1=""
        s2=""
        temp=""

        temp = re.findall(r'\d+', s)
        l = list(map(int, temp))

        temp=""

        for i in range(len(l)-1,-1,-1):
            
            indx=s.rindex(str(l[i]))
            print(indx)
            j=indx+len(str(l[i]))+1
            while (s[j]!=']'):
                
                print(j)
                s1+=s[j]
                j+=1
            k=1
            s2=s1
            
            print(s2,int(l[i]))
            while k<=int(l[i]):
                temp+=s1
                k+=1
            print(temp)
            s2=str(l[i])+'['+s2+']'
            print(s2,s1)
            t=len(s2)-len(s1)
            k=0
            while k<t:
                temp=temp+' '
                k+=1
            s=s.replace(s2,temp)
            
            print(s)
            s1=""
            temp=""
        s=s.replace(' ','')
        return(s)