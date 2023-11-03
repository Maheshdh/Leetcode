class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '9' : '6',
            '8' : '8'
        }
        res =""
        for i in str(n):
            if i in invert:
                res += invert[i]
            else:
                return False
        res = res[::-1]
        if n == int(res):
            return False
        else:
            return True
