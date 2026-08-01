from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_counts = Counter()
        left = 0
        max_length = 0

        for right, right_char in enumerate(s):
            char_counts[right_char] += 1

            while char_counts[right_char] > 1:
                left_char = s[left]
                char_counts[left_char] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
