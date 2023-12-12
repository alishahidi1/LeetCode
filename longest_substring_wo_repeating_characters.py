class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        # p2 = 1
        sub_s = set()
        lst_max = 0
        for char in s:
            while char in sub_s:
                sub_s.remove(s[p1])
                p1 += 1
            sub_s.add(char)
            lst_max = max(lst_max , len(sub_s))
        return lst_max
