class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        aset = {}
        res = set()

        for i, char in enumerate(s):
            if char not in aset:
                aset[char] = (i, i)
            else:
                (start, end) = aset[char]
                aset[char] = (start, i)

        for char in aset:
            (start, end) = aset[char]
            for i in range(start + 1, end):
                string = char + s[i] + char
                res.add(string)
                # print(f"i : {i}, j : {j}, string: {string}")

        return len(res)
