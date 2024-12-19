import re

class DayThree:
    def sum_multiplications_in_data(self, data):
      pattern = r"^[^d]*(?=do\(\)|don't\(\))|(?<=do\(\))[\s\S]*?(?=don't\(\))|(?<=do\(\))[\s\S]*"
      matches = re.findall(pattern, data)
      mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
      total_sum = 0
      for match in matches:
          mul_matches = re.findall(mul_pattern, match)
          total_sum += sum(int(x) * int(y) for x, y in mul_matches)

      return total_sum
