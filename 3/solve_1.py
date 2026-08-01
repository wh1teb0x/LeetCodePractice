from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0
        max_length = 0

        while right < len(s):
            r_char = s[right]
            chars[r_char] += 1

            while chars[r_char] > 1:
                l_char = s[left]
                chars[l_char] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
