from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Инициализируем переменную для хранения максимального расстояния
        max_distance = 0
        # Инициализируем переменную для хранения индекса последнего встреченного человека
        last_person = -1
        # Длина массива seats
        n = len(seats)

        # Проходим по каждому элементу массива seats
        for i in range(n):
            # Если текущий элемент - человек (1)
            if seats[i] == 1:
                # Если это первый встреченный человек
                if last_person == -1:
                    # Максимальное расстояние до ближайшего человека для всех предыдущих пустых мест равно i
                    max_distance = i
                else:
                    # Если это не первый человек, вычисляем расстояние до ближайшего человека для всех мест между last_person и текущим человеком
                    max_distance = max(max_distance, (i - last_person) // 2)
                # Обновляем last_person на текущий индекс
                last_person = i

        # Обработка хвоста массива, если последние места пустые
        if seats[n - 1] == 0:
            # Проверяем и обновляем max_distance, если расстояние от последнего человека до конца массива больше текущего max_distance
            max_distance = max(max_distance, n - 1 - last_person)

        # Возвращаем максимальное расстояние до ближайшего человека
        return max_distance


Solution().maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1])
