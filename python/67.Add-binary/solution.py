class Solution:

    def binToDec(self, s: str) -> int:

        dec = 0
        p = 0

        l = list(s)

        for c in reversed(l):
            if c == '1':
                dec += 2 ** p
            p += 1

        return dec

    def decToBin(self, dec: int) -> str:

        if dec == 0:
            return "0"

        s = ""

        while dec > 0:
            r = dec % 2
            dec = dec // 2

            s += '1' if r == 1 else '0'

        return s[::-1]

    def addBinary(self, a: str, b: str) -> str:

        a_dec = self.binToDec(a)
        b_dec = self.binToDec(b)

        return self.decToBin(a_dec + b_dec)
