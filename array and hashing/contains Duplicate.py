#contains Duplicate problem
#leetcode question number : 217
#using set /hashing
class solution1:
    def containsDuplicate(self,nums:list[int]):
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
sol1=solution1()
sol1.containsDuplicate([1,2,3,3])

class solution2:
    def hasDuplicate(self,nums):
        hashh={}
        for num in nums:
            if num in hashh:
                hashh[num]+=1
            else:
                hashh[num]=1
        for num in nums:
            if hashh[num]>1:
                return True
        return False
sol2=solution2()
sol2.hasDuplicate([1,2,3,4])