class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]=d[i]+1
            else:
                d[i]=1
        l=[]
        a1_sorted_keys = sorted(d, key=d.get, reverse=True)
        for r in a1_sorted_keys:
            print(r, d[r])
        sorted_dict = {i: d[i] for i in a1_sorted_keys}


        return(list(sorted_dict.keys())[0:k])