class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        going_down = False
        current_row = 0
        char_rows = [[] for _ in range(numRows)]

        for char in s:
            char_rows[current_row].append(char)
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        result = []
        for char_row in char_rows:
            result.extend(char_row)

        return "".join(result)
