class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        chars = list(s)
        res = []
        for i in range(0, len(chars)):
            res.append(len(chars))
        for i in range(0, len(chars)):
            if chars[i] == c:
                for j in range (0, i):
                    res[j] = min(res[j], i-j)
                for j in range (i, len(chars)):
                    res[j] = j - i
        return res