class Solution:
    def maxScore(self, s: str) -> int:
        int_array = [int(char) for char in s]

        leftsum = 1 if int_array[0] == 0 else 0
        rightsum = sum(int_array) - int_array[0]
        maxsum = leftsum + rightsum

        for i in range(1, len(s) - 1):
            if int(s[i]) == 1:
                rightsum -= 1
            elif int(s[i]) == 0:
                leftsum += 1
            print(f"{i} th - {s[i]} , leftsum:{leftsum}, rightsum:{rightsum} ")
            maxsum = max(leftsum + rightsum, maxsum)

        return maxsum
