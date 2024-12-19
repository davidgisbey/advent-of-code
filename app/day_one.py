from collections import Counter
from app.data.day_one_distances import DayOneDistances

class DayOne:
    def format_distance_data(self):
      lines = DayOneDistances.DISTANCE_DATA.strip().split("\n")
      array1 = [int(line.split()[0]) for line in lines]
      array2 = [int(line.split()[1]) for line in lines]

      return array1, array2

    def calculate_distance(self, array1, array2):
      array1.sort()
      array2.sort()
      return sum(abs(a - b) for a, b in zip(array1, array2))

    def calculate_similarity_score(self, array1, array2):
      counts = Counter(array2)
      return sum(counts[num] * num for num in array1 if num in counts)
