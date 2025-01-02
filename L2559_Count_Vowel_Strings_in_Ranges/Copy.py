class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(list("aeiou"))
        prefixCount = [0]+list(accumulate(1 if word[0] in vowels and word[-1] in vowels else 0 for word in words))
        print(prefixCount)
        return [prefixCount[end+1]-prefixCount[start] for start, end in queries]