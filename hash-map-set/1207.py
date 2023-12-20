# unique number of occurrences
def uniqueOccurrences(self, arr: List[int]) -> bool:
    hashmap = {}
    for element in arr:
        try:
            if hashmap[element]:
                hashmap[element] += 1
        except:
             hashmap[element] = 1
        
    h1 = list(hashmap.values())
    h2 = set(hashmap.values())
    return len(h1) == len(h2) 