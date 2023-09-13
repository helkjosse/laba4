import convert


def calculate(staff_number: int, staff_home_distances: list, taxi_number_and_tariff: dict) -> None:
    if len(staff_home_distances) != staff_number or len(taxi_number_and_tariff) != staff_number:
        print("Ошибка входных данных")
        return

    # Соединить каждого сотрудника с такси, отсортировать по расстоянию в порядке убывания
    staff = sorted(list(enumerate(staff_home_distances, start=1)), key=lambda x: x[1], reverse=True)

    # Сопоставить каждое такси с его тарифом, отсортировать по тарифам в порядке возрастания
    taxis = sorted(list(taxi_number_and_tariff.items()), key=lambda x: x[1])

    summ = 0
    assignments = [0] * staff_number

    for i in range(staff_number):
        employee, distance = staff[i]
        taxi, tariff = taxis[i]
        summ += distance * tariff
        assignments[employee - 1] = taxi  # Назначить это такси сотруднику
    # Вывести назначенное такси
    for i in range(staff_number):
        print(f'Работник № {i + 1} должен сесть в такси № {assignments[i]}')

    print(summ)
    print(convert.convert_number_to_words(summ))


if __name__ == '__main__':
    n = int(input("Введите количество работников, которым нужно заказать такси: "))

    n_dist = []

    for i in range(n):
        n_dist.append(int(input("Введите расстояние до дома для сотрудника №" + str(i + 1) + ": ")))

    t_tariff = {}

    for i in range(1, n + 1):
        value = int(input("Введите стоимость тарифа для такси №" + str(i) + ": "))
        t_tariff[i] = value

    calculate(n, n_dist, t_tariff)
