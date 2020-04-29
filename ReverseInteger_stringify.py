class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x >= 2**31-1:
            return 0
        else:
            x = str(x)
            if x[0] != "-":
                rev = x[::-1] 
            else:
                x = x[1:]
                rev = x[::-1]
                rev = "-" + rev
            if int(rev) < -2**31 or int(rev) > 2**31-1:
                return 0
            else: return int(rev)
