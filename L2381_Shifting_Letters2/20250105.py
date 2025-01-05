from collections import deque


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        delta_list = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            delta_list[start] += shift_value
            delta_list[end + 1] -= shift_value

        delta_acc = [0] * len(s)
        acc = 0
        for i in range(len(s)):
            acc += delta_list[i]
            delta_acc[i] = acc

        res = []
        for i, char in enumerate(s):
            shift = delta_acc[i]
            int_val = (ord(char) - ord('a') + shift) % 26 + ord('a')
            res.append(chr(int_val))

        return ''.join(res)