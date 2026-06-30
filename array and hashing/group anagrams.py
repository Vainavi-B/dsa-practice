#group anagrams
#leetcode question number:49
#hash map-list
from collections import defaultdict
class solution:
    def groupanagram(self,strs):
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())
sol=solution()
print(sol.groupanagram(["act","pots","tops","cat","stop","hat"]))

