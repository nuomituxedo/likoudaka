class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
        
        def backtrack(nums,targetLeft,path):
            
            #found a combination
            if targetLeft==0:
                res.append(path)
                return
            
            for i in range(len(nums)):
                #avoid duplicate combination
                if i>0 and nums[i]==nums[i-1]:
                    continue
                    
                #impossible to form a combination
                if nums[i]>targetLeft:
                    break
                
                #backtrack using the unvisited numbers, new target, and current
                backtrack(nums[i+1:],targetLeft-nums[i],path+[nums[i]])    
            
        res=[]
        backtrack(sorted(candidates),target,[])
        return res