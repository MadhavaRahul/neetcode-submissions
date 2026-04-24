class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram=False
        s=sorted(s)
        t=sorted(t)
        # for i in s:
        #     for j in t:
        if s==t:
            if len(s)==len(t):
                return True
            elif len(s)!=len(t):
                return False
            # return True
        # elif s!=t:
        #     return False
        return False


        