import pytest
from app.day_three import DayThree
from app.data.day_three_corrupted_data import DayThreeCorruptedData

def test_sum_multiplications_in_data_matches_multiply_with_up_to_three_digits_and_sums_them():
  data = "acmul(1,120)adad1!mul12345mul(100,5)adadad!$mul(10,4000)"
  assert DayThree().sum_multiplications_in_data(data) == 620

def test_sum_multiplications_in_data_works_with_provided_data():
  data = DayThreeCorruptedData.CORRUPTED_DATA
  assert DayThree().sum_multiplications_in_data(data) == 188116424
