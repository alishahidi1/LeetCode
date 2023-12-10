class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_1 = {}
        dct_2 = {}

        for char in s:
            if char in dct_1.keys():
                dct_1[char]+=1
            else:
                dct_1[char] = 1
        
        for char in t:
            if char in dct_2.keys():
                dct_2[char]+=1
            else:
                dct_2[char] = 1
        
        # if dct_1 == dct_2:
        #     return True
        # else:
        #     return False

        return dct_1 == dct_2
