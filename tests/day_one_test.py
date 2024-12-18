import pytest
from app.day_one import DayOne

def test_format_distance_data_returns_two_arrays_of_ints():
  array1, array2 = DayOne().format_distance_data()
  assert len(array1) > 0
  assert len(array2) > 0
  assert all(isinstance(el, int) for el in array1)
  assert all(isinstance(el, int) for el in array2)

def test_calculate_distance_sums_the_difference_between_elements_with_same_index():
  array1 = [3, 5]
  array2 = [1, 2]

  assert DayOne().calculate_distance(array1, array2) == 5

def test_calculate_distance_subtracts_the_smallest_number_from_the_largest_number_in_each_pair():
  array1 = [1, 2]
  array2 = [3, 5]

  assert DayOne().calculate_distance(array1, array2) == 5

def test_calculate_distance_sorts_arrays_before_calculation():
  array1 = [1, 2]
  array2 = [5, 3]

  assert DayOne().calculate_distance(array1, array2) == 5

def test_calculate_distance_gets_the_correct_answer_when_using_distance_data_variable():
  array1, array2 =  DayOne().format_distance_data()
  assert DayOne().calculate_distance(array1, array2) == 2196996
