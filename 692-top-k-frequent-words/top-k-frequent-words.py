class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        l=[]
        dict={}
        dict1={}
        sorted_dict={}
        s={}
        for i in words:
            if i in dict.keys():
                dict[i]=dict[i]+1
            else:
                dict[i]=1

        for i in sorted(dict.items(),key=lambda x: (-x[1],x[0])):
            if k>0:
                l.append(i[0])
                k-=1
        print(l)
        return(l)
