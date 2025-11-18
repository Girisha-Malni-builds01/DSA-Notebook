class Solution(object):
    def majorityElement(self, nums):
        c1 = c2 = None
        cnt1 = cnt2 = 0

        for n in nums:
            if n == c1:
                cnt1 += 1
            elif n == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1 = n; cnt1 = 1
            elif cnt2 == 0:
                c2 = n; cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        
        res = []
        for c in (c1, c2):
            if nums.count(c) > len(nums)//3:
                res.append(c)
        return res

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        