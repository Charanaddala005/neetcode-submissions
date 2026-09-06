class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        m = len(s)
        n = len(t)
        if m != n:
            return False

        count_s = {}
        count_t = {}

        for i in range(0,m):
            if s[i] in count_s:
                count_s[s[i]] = count_s[s[i]] + 1
            else:
                count_s[s[i]] = 1
        for j in range(0,n):
            if t[j] in count_t:
                count_t[t[j]] = count_t[t[j]] + 1
            else:
                count_t[t[j]] = 1
        if count_s == count_t:
            return True
       
        return False
