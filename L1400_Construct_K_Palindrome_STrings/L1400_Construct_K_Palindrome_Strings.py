class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # key idea
        # odd number of chars < k then true. else check i / 2 + j < k  (i is even numbers / j is odd numbers)

        count_dic = {}

        for char in s:
            if char not in count_dic:
                count_dic[char] = 0
            count_dic[char] += 1

        oddc = 0

        evensum = 0
        oddsum = 0
        for char, count in count_dic.items():
            print(f"{char}, {count}")
            if count % 2 == 0:
                evensum += count
            else:
                oddc += 1
                oddsum += count

        print(f"{oddc} {evensum} {oddsum}")

        return oddc <= k and evensum + oddsum >= k
