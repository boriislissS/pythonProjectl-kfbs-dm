import itertools

# задаємо матрицю відстаней
distances = [
    [0, 0, 69, 60, 10, 20],
    [0, 0, 0, 31, 39, 2],
    [69, 0, 0, 0, 59, 0],
    [60, 31, 0, 0, 0, 36],
    [10, 39, 59, 0, 0, 79],
    [20, 2, 0, 36, 79, 0]
]

# знаходимо всі можливі перестановки міст
cities = [i for i in range(len(distances))]
permutations = itertools.permutations(cities)

# знаходимо мінімальний маршрут та його відстань
min_distance = float("inf")
min_path = None
for path in permutations:
    distance = 0
    for i in range(len(path) - 1):
        distance += distances[path[i]][path[i + 1]]
    distance += distances[path[-1]][path[0]]  # доповнюємо маршрут до замкненого кола
    if distance < min_distance:
        min_distance = distance
        min_path = path

# виводимо результат
print(f"Мінімальна відстань: {min_distance}")
print(f"Маршрут: {' -> '.join(str(city) for city in min_path)} -> {min_path[0]}")
