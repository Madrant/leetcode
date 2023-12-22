class Solution:

    # O(n^2)
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

    # O(2n)
    def maxScore2(self, s: str) -> int:

        len_s = len(s)
        ones_total = s.count("1")

        l_score = 0
        r_score = ones_total

        if s[0] == "0":
            l_score += 1
        elif r_score >= 1:
            r_score -= 1

        max_score = l_score + r_score

        for i in range(1, len_s - 1):

            if s[i] == "0":
                l_score += 1
            else:
                r_score -= 1

            score = l_score + r_score

            if score > max_score:
                max_score = score

        return max_score
