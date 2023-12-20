# find highest altitude
def largestAltitude(self, gain: List[int]) -> int:
    max_alt = 0
    alt = 0
    for i in range(0, len(gain)):
        alt += gain[i]
        if max_alt < alt: max_alt = alt
    return max_alt
