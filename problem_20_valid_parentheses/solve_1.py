class Solution:
    def isValid(self, s: str) -> bool:
        characters_mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for character in s:
            if character in characters_mapping:
                top_element = stack.pop() if stack else "#"
                if characters_mapping[character] != top_element:
                    return False

            else:
                stack.append(character)

        return not stack
