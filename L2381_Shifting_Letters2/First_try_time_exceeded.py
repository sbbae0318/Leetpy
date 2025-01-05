class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        ilist = []
        for c in s:
            ilist.append(ord(c))

        for shift in shifts:
            direction = 1
            if shift[2] == 0:
                direction = -1
            for i in range(shift[0], shift[1] + 1):
                ilist[i] = ilist[i] + direction

                if ilist[i] > 122:
                    ilist[i] = ord('a')
                elif ilist[i] < 97:
                    ilist[i] = ord('z')

        res = ""
        for i in ilist:
            res += chr(i)

        return res
