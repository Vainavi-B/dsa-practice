#top k frequent elements
#leetcode question number:347
#hashmap-list
from collections import defaultdict
class solution:
    def topKfrequent(self,nums,k):
        hashh=defaultdict(int)
        for num in nums:
            hashh[num]+=1
        bucket=defaultdict(list)
        for i in hashh:
            freq=hashh[i]
            bucket[freq].append(i)
        res=[]
        n=len(nums)
        for freq in range(n,0,-1):
            for num in bucket[freq]:
                res.append(num)
                if len(res)==k:
                    return res
sol=solution()
print(sol.topKfrequent([1,1,1,2,2,3],2))