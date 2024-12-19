import pytest
from app.day_four import DayFour

def test_format_report_data_returns_140_rows_strings():
  formatted_data = DayFour().format_crossword_data()
  first_row = formatted_data[0]
  allowed_chars = ["X", "M", "A", "S"]
  assert len(formatted_data) == 140
  assert all(el in allowed_chars for el in first_row)

def test_detect_xmas_works_horizontally_ltr():
  data = [
          ["X", "M", "A", "S", "X", "S", "X", "M", "A", "S"],
          ["X", "M", "A", "S", "X", "S", "X", "M", "A", "S"],
         ]
  assert(DayFour().detect_xmas_count(data)) == 4

def test_detect_xmas_works_horizontally_ltr_handles_x_being_in_list_3_letters_gracefully():
  data = [
    ["S","A","A","X"],
    ["S","A","X","M"],
    ["A","X","M","A"],
    ["X","M","A","S"],
  ]

  assert(DayFour().detect_xmas_count(data)) == 1

def test_detect_xmas_works_horizontally_rtl():
  data = [
           ["S","A","M","X"],
           ["S","A","X","M"],
           ["A","X","M","A"],
           ["X","M","A","M"],
         ]
  assert(DayFour().detect_xmas_count(data)) == 1
