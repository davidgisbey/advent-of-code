import pytest
from app.day_two import DayTwo

def test_format_report_data_returns_1000_reports_of_nested_arrays_of_ints():
  formatted_data = DayTwo().format_report_data()
  assert len(formatted_data) == 1000
  assert all(isinstance(el, int) for el in formatted_data[0])

def test_calculate_safe_reports_identifies_incrementing_reports_as_safe():
  reports = [[1,2,5,6,7]]
  assert DayTwo().calculate_safe_reports(reports) == 1

def test_calculate_safe_reports_identifies_decrementing_reports_as_safe():
  reports = [[8,7,6,4,2]]
  assert DayTwo().calculate_safe_reports(reports) == 1

def test_calculate_safe_reports_identifies_reports_with_identical_consecutive_ints_as_safe():
  reports = [[1,1,2,4,5]]
  assert DayTwo().calculate_safe_reports(reports) == 1

def test_calculate_safe_reports_identifies_reports_with_multiple_identical_consecutive_ints_as_unsafe():
  reports = [[1,1,2,2,4,5]]
  assert DayTwo().calculate_safe_reports(reports) == 0

def test_calculate_safe_reports_doesnt_count_reports_that_increment_by_more_than_three_as_safe():
  reports = [[1,5,6]]
  assert DayTwo().calculate_safe_reports(reports) == 1

def test_calculate_safe_reports_identifies_reports_that_increment_by_more_than_three_twice_as_unsafe():
    reports = [[1,5,9]]
    assert DayTwo().calculate_safe_reports(reports) == 0

def test_calculate_safe_reports_doesnt_count_reports_that_decrement_by_more_than_three_as_safe():
  reports = [[6,5,1]]
  assert DayTwo().calculate_safe_reports(reports) == 1

def test_calculate_safe_reports_identifies_reports_that_decrement_by_more_than_three_twice_as_unsafe():
    reports = [[9,5,1]]
    assert DayTwo().calculate_safe_reports(reports) == 0

def test_calculate_safe_reports_gets_the_correct_answer_when_using_report_data():
  reports = DayTwo().format_report_data()
  assert DayTwo().calculate_safe_reports(reports) == 311

def test_calculate_safe_reports_two_unsafe_levels_are_unsafe():
  reports1 = [[7, 6, 4, 2, 1]]
  reports2 = [[1, 2, 7, 8, 9]]
  reports3 = [[9, 7, 6, 2, 1]]
  reports4 = [[1, 3, 2, 4, 5]]
  reports5 = [[8, 6, 4, 4, 1]]
  reports6 = [[1, 3, 6, 7, 9]]

  assert DayTwo().calculate_safe_reports(reports1) == 1
  assert DayTwo().calculate_safe_reports(reports2) == 0
  assert DayTwo().calculate_safe_reports(reports3) == 0
  assert DayTwo().calculate_safe_reports(reports4) == 1
  assert DayTwo().calculate_safe_reports(reports5) == 1
  assert DayTwo().calculate_safe_reports(reports6) == 1
