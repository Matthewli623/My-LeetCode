class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d={}
        
        for num in nums:
            if num in d:
                d[num]=d[num]+1
            else:
                d[num]=1
                
        sd=sorted(d.items(),key=lambda x:x[1],reverse=True)
        
        ans=[]
        
        for i in range(k):
            ans.append(sd[i][0])
            
        return ans