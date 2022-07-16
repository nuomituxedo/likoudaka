class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        last_c = 0
        for i in range(0, len(s)):
            res.append(len(s))
        for i in range(0, len(s)):
            if s[i] == c:
                #update left hand side up to the last seen c
                for j in range (last_c, i):
                    res[j] = min(res[j], i-j)
                last_c = i
                #update right hand side
                for j in range (i, len(s)):
                    res[j] = j - i
                    # stop updating right side if see next c
                    if s[j] == c:
                        continue
        return res