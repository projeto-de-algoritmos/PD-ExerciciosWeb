class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n  # Dynamic programming array to store the longest substring length ending at each index
        dp[0] = 1
        max_len = 1

        # Dictionary to store the most recent occurrence index of each character
        char_index = {s[0]: 0}

        for i in range(1, n):
            if s[i] in char_index:
                # If the current character is already seen, update the start index of the substring
                start = char_index[s[i]] + 1
                # Update the most recent occurrence index of the character
                char_index[s[i]] = i
                # Update the longest substring length ending at the current index
                dp[i] = i - start + 1
            else:
                # If the current character is new, add it to the dictionary
                char_index[s[i]] = i
                # Update the longest substring length ending at the current index
                dp[i] = dp[i - 1] + 1

            # Update the maximum length if necessary
            max_len = max(max_len, dp[i])

        return max_len
