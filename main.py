import convert


def calculate(staff_number: int, staff_home_distances: list, taxi_number_and_tariff: dict) -> None:
    if len(staff_home_distances) != staff_number or len(taxi_number_and_tariff) != staff_number:
        print("Ошибка входных данных")
        return

    staff_home_distances.sort(reverse=True)

    sorted_taxi_number_and_tariff = {k: v for k, v in sorted(taxi_number_and_tariff.items(),
                                                             key=lambda item: item[1])}
    index = 0
    summ = 0

    for elements in sorted_taxi_number_and_tariff.items():
        print(elements[0])

        summ += elements[1] * staff_home_distances[index]
        index += 1

    print(summ)
    print(convert.convert_number_to_words(summ))


def test1():
    print("Тест 1")
    staff_n = 3
    staff_h_d = [20, 40, 60]
    taxi_n_t = {1: 40, 2: 10, 3: 20}
    calculate(staff_n, staff_h_d, taxi_n_t)


def test2():
    print("Тест 2")
    staff_n = 5
    staff_h_d = [5, 10, 1, 15, 15]
    taxi_n_t = {1: 3, 2: 3, 3: 3, 4: 2, 5: 3}
    calculate(staff_n, staff_h_d, taxi_n_t)


def test3():
    print("Тест 3")
    staff_n = 1
    staff_h_d = []
    taxi_n_t = {5: 130}
    calculate(staff_n, staff_h_d, taxi_n_t)


if __name__ == '__main__':
    test1()
    test2()
    test3()

    n = int(input("Введите количество работников, которым нужно заказать такси: "))

    n_dist = []

    for i in range(n):
        n_dist.append(int(input("Введите расстояние до дома для сотрудника №" + str(i + 1) + ": ")))

    t_tariff = {}

    for i in range(1, n + 1):
        value = int(input("Введите стоимость тарифа для такси №" + str(i) + ": "))
        t_tariff[i] = value

    calculate(n, n_dist, t_tariff)
