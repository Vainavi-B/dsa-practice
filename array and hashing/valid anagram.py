#valid anagram
#leetcode question number: 242
#hashing 
class Solution1:
    def validanagram(self,s:str,t:str):
        if len(s)!=len(t):
            return False
        dict1={}
        dict2={}
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in t:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
        if dict1==dict2:
            return True
        else:
            return False
sol1=Solution1()
sol1.validanagram("racecar","carrace")

from collections import Counter
class solution2():
    def validanagram(self,s:int,t:int):
        return Counter(s)==Counter(t)
sol2=solution2()
sol2.validanagram("car","cat")