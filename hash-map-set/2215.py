# find the difference of two arrays
def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    ans1 = set([n for n in nums1 if n not in nums2])
    ans2 = set([n for n in nums2 if n not in nums1])
    return [ans1,ans2]
