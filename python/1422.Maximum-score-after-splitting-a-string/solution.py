class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0

        for i in range(1, len(s)):

            l = s[:i]
            r = s[i:]

            l_score = l.count("0")
            r_score = r.count("1")

            score = l_score + r_score

            if score > max_score:
                max_score = score

        return max_score
