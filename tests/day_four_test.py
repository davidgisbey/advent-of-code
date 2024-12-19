import pytest
from app.day_four import DayFour

def test_format_report_data_returns_140_rows_strings():
  formatted_data = DayFour().format_crossword_data()
  first_row = formatted_data[0]
  allowed_chars = ["X", "M", "A", "S"]
  assert len(formatted_data) == 140
  assert all(el in allowed_chars for el in first_row)
