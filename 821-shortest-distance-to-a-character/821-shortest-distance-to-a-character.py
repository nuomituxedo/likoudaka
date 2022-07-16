class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        chars = list(s)
        res = []
        last_c = 0
        for i in range(0, len(chars)):
            res.append(len(chars))
        for i in range(0, len(chars)):
            if chars[i] == c:
                for j in range (last_c, i):
                    res[j] = min(res[j], i-j)
                last_c = i
                for j in range (i, len(chars)):
                    res[j] = j - i
                    # stop updating right side if see next c
                    if chars[j] == c:
                        continue
        return res