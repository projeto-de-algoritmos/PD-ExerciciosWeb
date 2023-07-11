from collections import Counter

class Solution:
    def largestVariance(self, s: str) -> int:
        max_variance = 0

        for i in range(len(s)):
            count = Counter()
            max_count = 0

            for j in range(i, len(s)):
                count[s[j]] += 1
                max_count = max(max_count, count[s[j]])
                min_count = min(count.values())
                max_variance = max(max_variance, max_count - min_count)

        return max_variance