class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        intSum = romanDict[s[len(s)-1]]
        for i in range(len(s)-1, 0, -1):
            cur = romanDict[s[i]]
            pre = romanDict[s[i-1]]
            if pre >= cur :
                intSum += pre
            else:
                intSum -= pre
        return intSum
