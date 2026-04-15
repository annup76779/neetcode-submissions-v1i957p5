class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        if len(s) != len(t):
            return False

        for i, j in zip(s, t):
            if i in freq_s:
                freq_s[i] += 1
            else:
                freq_s[i] = 1
            
            if j in freq_t:
                freq_t[j] += 1
            else:
                freq_t[j] = 1

        return freq_s == freq_t