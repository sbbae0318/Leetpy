

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        pref = p = s = 0
        #s : 앞에 있던 S갯수
        #p : 뒤에 아직 남아있는 P갯수
        #pref : 계산된 움직임 횟수

        # 0 인덱스에 pref를 미리 계산하고, 한칸 넘어갈 때마다 1일때 / 아닐때 나눠서 계산할수있음. (association 사용)
        for i, el in enumerate(boxes):
            if el == '1':
                pref += i
                p += 1
        for el in boxes:
            answer.append(pref)
            if el == '1':
                p -= 1
                s += 1
            pref = pref - p + s
        return answer