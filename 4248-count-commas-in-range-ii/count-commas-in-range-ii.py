class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        if n >= 1_000:
            ans += n - 1_000 + 1

        if n >= 1_000_000:
            ans += 1_000_000 * 2 - 1_000_000 * 1
            ans += (min(n, 999_999_999) - 1_000_000 + 1) * 1

        # Easier general solution:
        ans = 0
        start = 1_000
        commas = 1

        while start <= n:
            end = start * 1000 - 1
            count = min(n, end) - start + 1
            ans += count * commas

            start *= 1000
            commas += 1

        return ans


        