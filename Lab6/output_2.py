class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        """
        Обчислює суму та кількість елементів даних.
        """
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def calculate_total(self):
        """
        Обчислює суму елементів даних.
        """
        total, _ = self._calculate_total_and_count()
        return total

    def calculate_average(self):
        """
        Обчислює середнє значення даних.
        """
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_minimum(self):
        """
        Обчислює мінімальне значення даних.
        """
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        """
        Обчислює максимальне значення даних.
        """
        return max(self.data) if self.data else None