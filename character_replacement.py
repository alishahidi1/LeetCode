class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        # r = 0
        dct = {}
        maxf = 0
        res = 0

        for r in range(len(s)):
            if s[r] in dct.keys():
                dct[s[r]] += 1
            else:
                dct[s[r]] = 1
            maxf = max(maxf, dct[s[r]])
        
            leng = r - l + 1
            if leng - maxf > k:
                dct[s[l]] -= 1
                l += 1 
        return r - l + 1
