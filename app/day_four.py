from app.data.day_four_crossword import DayFourCrossword

class DayFour:
    def format_crossword_data(self):
      lines = DayFourCrossword.CrossWord.strip().split("\n")
      return [list(line) for line in lines]

    def detect_xmas_count(self, data):
      count = 0
      count += self.__check_row_rtl_count(data)
      return count

    def __check_row_rtl_count(self, data):
      count = 0
      for row in data:
         for index, letter in enumerate(row):
            if letter == "X":
               if index + 3  >= len(row):
                  continue

               letters = [letter, row[index + 1], row[index + 2], row[index + 3]]
               if "".join(letters) == "XMAS":
                  count += 1

      return count
