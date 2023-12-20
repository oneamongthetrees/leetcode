# find pivot index
def pivotIndex(self, nums: List[int]) -> int:
    ls = 0
    rs = sum(nums)

    for i in range(len(nums)):
        if i != 0: ls += nums[i-1]
        rs -= nums[i]
        if ls == rs: return i
        
    return -1