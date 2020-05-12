class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        a = sorted(costs,key= lambda x :x[0]-x[1])
        res=0
        left = 0
        right = 0
        for b in a:
            if left >=len(a)//2:
                res+=b[1]
                right+=1
            elif right >=len(a)//2:
                res+=b[0]
                right+=1
            else :
                res+=b[0]
                left+=1
        return res
                
                
        