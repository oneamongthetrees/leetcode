# kids with the greatest number of candies
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    kids = [False for _ in range(len(candies))]
    for i in range(len(candies)):
        if candies[i]+extraCandies>=max_candies:
            kids[i] = True
    return kids