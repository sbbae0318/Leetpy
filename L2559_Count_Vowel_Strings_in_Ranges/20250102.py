# 풀이 설명
# 각 단어가 모음인지 아닌지 판별해서 리스트를 만든다
# 해당 리스트를 accumulate해서 빼면 각 구간에 해당하는 모음 단어의 개수를 구할 수 있다
# 적당한 인덱스 보정이 필요함.`

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowel(cv: chr) -> bool:
            if cv == 'a' or cv == 'e' or cv == 'i' or cv == 'o' or cv == 'u':
                return True
            return False

        list1 = [0]
        for sv in words:
            if isVowel(sv[0]) and isVowel(sv[-1]):
                list1.append(1)
            else:
                list1.append(0)

        # print(f"{list1}")

        sumval = 0
        for i in range(0, len(list1)):
            list1[i] = list1[i] + sumval
            sumval = list1[i]
        #    print(f"- {sumval}")

        # print(f"{list1}")

        res = []
        for qpair in queries:
            # print(f"-{qpair[1]} - {qpair[0]}")
            val = list1[qpair[1] + 1] - list1[qpair[0]]
            res.append(val)

        return res
