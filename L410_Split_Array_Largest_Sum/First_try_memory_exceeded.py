from collections import deque

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        res = 99999999

        q = deque()
        sv = 0
        for i in range(0, len(nums)):
            sv += nums[i]
            q.append((sv, i + 1, k - 1))

        while len(q) > 0:
            (sumval, index, n) = q.popleft()

            if index == len(nums) and n > 0:
                continue
            if n == 0 and index < len(nums):
                continue
            if n == 0 and index == len(nums):
                res = min(res, sumval)
                continue

            sv = 0
            for i in range(index, len(nums)):
                sv += nums[i]
                newval = max(sumval, sv)
                q.append((newval, i + 1, n - 1))

        return res

