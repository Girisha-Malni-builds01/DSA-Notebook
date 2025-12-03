class Solution:
    def runningSum(self,nums:List[int])-> List[int]:
        sum=0
        result=[]
        for num in nums:
            sum+=num
            result.append(sum)
        return result