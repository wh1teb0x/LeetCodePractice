class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        row_chars = [[] for _ in range(numRows)]
        current_row = 0
        going_down = False

        for char in s:
            row_chars[current_row].append(char)

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        result = []
        for char_list in row_chars:
            result.extend(char_list)

        return "".join(result)
