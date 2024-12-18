import pytest
from app.day_two import DayTwo

def test_format_report_data_returns_nested_arrays_of_ints():
  formatted_data = DayTwo().format_report_data()
  assert len(formatted_data) == 1000
  assert all(isinstance(el, int) for el in formatted_data[0])
