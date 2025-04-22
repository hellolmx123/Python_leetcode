class NumArray:
    def __init__(self, nums: list[int]):
        s=[0]*(len(nums)+1)
        for i in range(len(nums)):
            s[i+1]=nums[i]+s[i]
        self.nums=s
    def sumRange(self, left: int, right: int) -> int:
        print(self.nums[right+1]-self.nums[left])
        return self.nums[right+1]-self.nums[left]
nums=[-2, 0, 3, -5, 2, -1]
NumArray.__init__(NumArray,nums)
NumArray.sumRange(NumArray,0,2)
NumArray.sumRange(NumArray,2,5)
NumArray.sumRange(NumArray,0,5)