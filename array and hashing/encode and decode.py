#encode-decode 
#leetcode problem number: 271
#array-string slicing
class Solution:

    def encode(self, strs: list[str]) -> str:
        
        string=""
        for s in strs:
            string+=str(len(s))+"#"+s
        return string

    def decode(self, s: str) -> list[str]:
        i=0
        decodelist=[]
        while i <len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            decodelist.append(s[j+1:j+1+length])
            i=j+length+1
        return decodelist

sol=Solution()
print(sol.encode(["hello","hehe","world","welcome","back"]))
print(sol.decode(sol.encode(["hello","hehe","world","welcome","back"])))

    