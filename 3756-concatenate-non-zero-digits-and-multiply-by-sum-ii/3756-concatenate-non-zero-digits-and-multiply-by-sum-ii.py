from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] * 10 % MOD

        N = 1
        while N < n:
            N <<= 1
        t = [(0, 0, 0)] * (2 * N)

        for i, c in enumerate(s):
            if c != '0':
                d = ord(c) - 48
                t[N + i] = (d, 1, d)

        def mg(a, b):
            return ((a[0] * p[b[1]] + b[0]) % MOD,
                    a[1] + b[1],
                    a[2] + b[2])

        for i in range(N - 1, 0, -1):
            t[i] = mg(t[i * 2], t[i * 2 + 1])

        ans = []
        for l, r in queries:
            l += N
            r += N
            L = (0, 0, 0)
            R = (0, 0, 0)
            while l <= r:
                if l & 1:
                    L = mg(L, t[l])
                    l += 1
                if not (r & 1):
                    R = mg(t[r], R)
                    r -= 1
                l //= 2
                r //= 2
            x, _, sm = mg(L, R)
            ans.append(x * sm % MOD)
        return ans
        