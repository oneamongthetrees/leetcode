# maximum average subarray I
def findMaxAverage(self, nums: List[int], k: int) -> float:
    x = sum(nums[0:k])
    m = x

    for i in range(len(nums)-k):
        x += nums[i+k] - nums[i]
        m = max(m, x)
    return m / k 