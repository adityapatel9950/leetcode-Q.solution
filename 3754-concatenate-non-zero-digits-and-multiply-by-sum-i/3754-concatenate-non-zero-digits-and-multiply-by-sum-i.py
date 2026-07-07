class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0

        s = str(n).replace("0", "")
        x = int(s) if s else 0

        for digit in str(n):
            total += int(digit)

        result = x * total
        return result