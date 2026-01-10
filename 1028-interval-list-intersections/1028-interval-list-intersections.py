class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        i,j = 0,0
        result = []


        while i < n and j < m:
            a1,a2 = firstList[i]
            b1,b2 = secondList[j]

            # Overlap:
            if a1 <= b2 and b1 <= a2:
                start = max(a1,b1)
                end = min(a2,b2)
                result.append([start, end])
            
            if b2 > a2:
                i += 1
            else:
                j += 1

        return result