from app.data.day_four_crossword import DayFourCrossword

class DayFour:
    def format_crossword_data(self):
      lines = DayFourCrossword.CrossWord.strip().split("\n")
      return [list(line) for line in lines]

