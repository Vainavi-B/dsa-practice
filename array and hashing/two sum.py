#twosum problem
#leetcode question number:1
#hash map
class Solution(object):
    def twosum(self,nums,target):
        prevmap={}
        for i in range(len(nums)):
            if target-nums[i] in prevmap:
                return [prevmap[target-nums[i]],i]
            prevmap[nums[i]]=i
        return []
sol=Solution()
print(sol.twosum([2,1,4,3],5))