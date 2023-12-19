# merge strings alternatively
def mergeAlternately(self, word1: str, word2: str) -> str:
    s = ''
    if len(word1) == len(word2):
        for a,b in zip(word1,word2):
            s += a; s += b;
    else:
        rng = min(len(word1), len(word2))
        for i in range(rng):
            s += word1[i]; s += word2[i];
        if len(word1) > len(word2):
            s += word1[rng:]
        else:
            s += word2[rng:]
        return s