import pytest
from app.day_three import DayThree
from app.data.day_three_corrupted_data import DayThreeCorruptedData

def test_sum_multiplications_in_data_matches_multiply_with_up_to_three_digits_and_sums_them():
  data = "do()acmul(1,120)adad1!mul12345mul(100,5)adadad!$mul(10,4000)don't()"
  assert DayThree().sum_multiplications_in_data(data) == 620

def test_sum_multiplications_in_data_only_captures_muls_between_do_and_donts():
  data = "do()mul(1,120)don't() mul(1,20) do()mul(100,5)don't() do()mul(10,4000)don't()"
  assert DayThree().sum_multiplications_in_data(data) == 620

def test_sum_multiplications_in_data_works_if_there_is_not_a_dont_function():
  data = "do()acmul(1,120)adad1!mul12345mul(100,5)adadad!$mul(10,4000)"
  assert DayThree().sum_multiplications_in_data(data) == 620

def test_sum_multiplications_in_data_works_with_provided_data():
  data = DayThreeCorruptedData.CORRUPTED_DATA
  assert DayThree().sum_multiplications_in_data(data) == 104245808
