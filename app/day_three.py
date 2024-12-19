import re

class DayThree:
    def sum_multiplications_in_data(self, data):
      pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
      matches = re.findall(pattern, data)
      return sum(int(x) * int(y) for x, y in matches)

