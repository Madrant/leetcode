class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:

        # Python one liner:
        return haystack.find(needle)

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:

        # Corner cases
        if len(needle) > len(haystack):
            return -1

        # Search substring until the end of haystack
        i = 0

        while i <= (len(haystack) - len(needle)):
            while haystack[i] != needle[0] and i < (len(haystack) - len(needle)):
                i += 1

            if i > (len(haystack) - len(needle)):
                return -1

            if haystack[i:i + len(needle)] == needle:
                return i
            else:
                i += 1

        return -1

class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:

        # Python one liner:
        # return haystack.find(needle)

        # Corner cases
        if len(needle) > len(haystack):
            return -1

        # Search substring until the end of haystack
        i = 0

        while i <= (len(haystack) - len(needle)):
            while haystack[i] != needle[0] and i < (len(haystack) - len(needle)):
                i += 1

            if i > (len(haystack) - len(needle)):
                return -1

            # if haystack[i:i + len(needle)] == needle:
            substring_found = True
            j = 0

            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    substring_found = False
                    break

            if substring_found:
                return i
            else:
                i += 1

        return -1
