from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_substring = 1
        counter = defaultdict(int)
        left, right = 0, 1

        counter[s[left]] = 1
        while right < len(s):
            counter[s[right]] += 1
            if counter[s[right]] == 1:
                max_substring = max(max_substring, right - left + 1)
            else:
                counter[s[left]] -= 1
                left += 1
            right += 1

        return max_substring
