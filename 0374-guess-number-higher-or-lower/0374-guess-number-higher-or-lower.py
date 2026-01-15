# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n

        while l <= r:
            start = (l + r) // 2
            response = guess(start)
            if response == -1:
                r = start-1 
            elif response == 1:
                l = start+1
            else:
                return start
