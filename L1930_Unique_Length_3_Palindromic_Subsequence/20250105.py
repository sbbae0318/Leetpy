class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        aset = {}
        res = set()

        for i, char in enumerate(s):
            # print(f"char: {char}, i: {i}")

            if char not in aset:
                aset[char] = i
                # print(f"{aset}")
            else:
                # print(f"{aset[char]}")
                for j in range(aset[char] + 1, i):
                    string = char + s[j] + char
                    res.add(string)
                    aset[char] = i - 1  # Timeout을 막기 위해 필요함.
                    # print(f"i : {i}, j : {j}, string: {string}")

        return len(res)