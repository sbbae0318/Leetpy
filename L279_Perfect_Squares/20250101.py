import math
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        res = 99999

        q = deque()
        q.append((n, 0))

        n2 = n
        while len(q) > 0:
            n2, cnt = q.popleft()

            sqv = math.floor(math.sqrt(n2))
            # print(f"n2: {n2}, sqv: {sqv}")

            for i in range(1, sqv + 1):
                if i * i == n2:
                    return cnt + 1

                # print(f"{n2}, {n2 - i*i}, {cnt + 1}")
                q.append((n2 - i * i, cnt + 1))

        return res
