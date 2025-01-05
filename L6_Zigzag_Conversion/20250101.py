class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = []

        r = 0
        reverse = False

        for i in range(0, len(s)):
            if reverse == False:
                list.append((s[i], i, r))
                r += 1
            else:
                list.append((s[i], i, r))
                r -= 1

            if r == numRows - 1:
                reverse = True
            elif r == 0:
                reverse = False

        print(list)

        sorted_list = sorted(list, key=lambda x: (x[2], x[1]))

        res = ""
        for x1, x2, x3 in sorted_list:
            res = res + x1

        print(sorted_list)

        return res