class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix = [0]
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
        # print(self.prefix)


    def sumRange(self, left: int, right: int) -> int:
        ans = self.prefix[right + 1] - self.prefix[left]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)