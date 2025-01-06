class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ilist = []
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == '1':
                ilist.append(i)

        for i in range(len(boxes)):
            for j in range(len(ilist)):
                res[i] += abs(i - ilist[j])
                # print(f"{i}, {j} {res[i]}")

        return res

