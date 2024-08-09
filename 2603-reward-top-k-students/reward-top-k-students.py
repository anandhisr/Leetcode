class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        d={}
        dg={}
        db={}
        for i in positive_feedback:
            dg[i]=3
        for i in negative_feedback:
            dg[i]=-1
        
        k1=0
        for i in report:
            score=0
            sid=student_id[k1]
            for j in i.split():
                
                if j in dg.keys():
                    score+=dg[j]
                elif j in db.keys():
                    score+=db[j]
            k1+=1
            
            d[sid]=score
        print(d)
        sorted_dict= sorted(d.items(),key=lambda x:(-x[1],x[0]))
        l=[]
        cnt=0
        while cnt<k:
            l.append(sorted_dict[cnt][0])
            cnt+=1            
        return(l)