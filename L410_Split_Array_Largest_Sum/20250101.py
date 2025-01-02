
# Difficulty: Hard
# Binary Search with a twist
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m, nums, k):
            arrays = 1
            sumval = 0
            dbgarray = []

            for i in range(0, len(nums)):
                if nums[i] > m:
                    return -1

                # print(f"sv: {sumval}, {i}, {arrays}")

                if sumval + nums[i] > m:
                    arrays += 1
                    dbgarray.append(sumval)


                    # print(f"appended {sumval}")
                    sumval = 0
                sumval += nums[i]

            dbgarray.append(sumval)

            # print(f"{k}, {arrays}, {dbgarray}")

            return k - arrays

        l = 0
        r = sum(nums)

        res = 0

        if k == 1:
            return r

        while l < r:
            m = (l + r) // 2

            # print(f"{m}, {l}, {r}")
            possible = check(m, nums, k)

            if possible < 0:
                l = m + 1
            else:
                r = m
                res = r

        return res