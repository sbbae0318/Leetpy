class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        rset = set()

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    rset.add(str(i) + str(j))

        return len(rset)
