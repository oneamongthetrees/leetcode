# greatest common divisor of strings
def gcdOfStrings(self, str1: str, str2: str) -> str:
    if str2+str1!=str1+str2: return ''
    elif str2 == '': return str1
     else:
        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1[:len(str1)%len(str2)])
        else:
            return self.gcdOfStrings(str1, str2[:len(str2)%len(str1)])