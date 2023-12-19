# reverse vowels of a string
def reverseVowels(self, s: str) -> str:
    vs = 'AEIOUaeiou'
    s = list(s)
    st = []
    for i in range(len(s)):
        if s[i] in vs: 
            st.append(s[i])
    
    for i in range(len(s)-1, -1, -1):
        if s[i] in vs:
            s[i] = st.pop(0)
    return ''.join(s)