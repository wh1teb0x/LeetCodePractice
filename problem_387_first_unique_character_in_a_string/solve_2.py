from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_counter = Counter()

        for c in s:
            character_counter[c] += 1

        for i in range(len(s)):
            if character_counter[s[i]] == 1:
                return i

        return -1
