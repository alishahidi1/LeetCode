class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        c_to_w = {}
        w_to_c = {}

        for c, w in zip(pattern, words):
            if c in c_to_w and c_to_w[c] != w:
                return False
            if w in w_to_c and w_to_c[w] != c:
                return False
            c_to_w[c] = w
            w_to_c[w] = c
        return True

