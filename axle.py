from typing import Any


# from math import tan


class MachineWithAxles:
    """
    Имитация машины с разным количеством осей

    """

    def __init__(self, len_bridge: int, axle_list: list, load_list: list, *args_prop) -> None:
        self.axle_in_car = [AxlesInTheBridge(num + 1, x_axle) for num, x_axle in
                            enumerate(zip(axle_list, load_list))]
        self.len_way = len_bridge
        self.len_bridge = len_bridge + max(self.axle_in_car).axle * 2
        self.distance_bridge = self.set_list_travel()
        self.distance_prop = self.set_list_travel(args_prop[0], args_prop[1])

    def __str__(self) -> str:
        """
        Возвращает координаты осей нагрузку моста в точках координат,
        произведение нагрузки моста веса оси машины на точку координат,
        исходя из максимальной нагрузки на мост осями
#
        :return: str
        """
        return "{}{}".format(self.str_bridge(), self.str_prop())

    def str_bridge(self):
        temp_bridge = self.sum_load(self.distance_bridge)
        coordinate_bridge = [x[0] for x in temp_bridge[0]]
        point_load_bridge = [x[1] for x in temp_bridge[0]]
        axles_load_bridge = [x[2] for x in temp_bridge[0]]
        return '\nНагрузка на мост:\n' \
               'Координаты осей - {coordinates_b},\n' \
               'нагрузки моста в этих точках - {point_load_b},\n' \
               'нагрузка осей в данных координатах - {axles_load_b},\n' \
               'наибольшая сумма нагрузок осей на мост - {sum_loads_b}\n'. \
            format(coordinates_b=coordinate_bridge,
                   point_load_b=point_load_bridge,
                   axles_load_b=axles_load_bridge,
                   sum_loads_b=temp_bridge[1]
                   )

    def str_prop(self):
        temp_prop = self.sum_load(self.distance_prop)
        coordinate_prop = [x[0] for x in temp_prop[0]]
        point_load_prop = [x[1] for x in temp_prop[0]]
        axles_load_prop = [x[2] for x in temp_prop[0]]
        return '\nНагрузка на опоры:\n' \
               'Координаты осей - {coordinates_p},\n' \
               'нагрузки моста в этих точках - {point_load_p},\n' \
               'нагрузка осей в данных координатах - {axles_load_p},\n' \
               'наибольшая сумма нагрузок осей на мост - {sum_loads_p}\n'. \
            format(coordinates_p=coordinate_prop,
                   point_load_p=point_load_prop,
                   axles_load_p=axles_load_prop,
                   sum_loads_p=temp_prop[1],
                   )

    def display_info_load_bridge(self) -> None:
        """
        Дорабатывается
        Выводит список нагрузок моста под осями,
        координаты нахождения осей,
        и произведение нагрузок моста и давления осей на точки координат

        :return:
        """
        count = 0
        self.display_car()
        for elem_t in self.distance_bridge:
            if any(elem_t):
                try:  # попытка избежать ошибки отсутствия Индекса
                    if elem_t[count][1] == 0.5:
                        print('На мост заезжает: {}'.format(self.axle_in_car[count]))  # Необходимо доработать
                        count += 1
                except IndexError:
                    pass
                print(elem_t)
        print()
        print(self.display_load_all_axles(self.distance_bridge))

    def display_info_load_prop(self) -> None:
        """
        Выводит список нагрузок моста под осями,
        координаты нахождения осей,
        и произведение нагрузок моста и давления осей на точки координат
        по обоим критериям

        :return: None
        """
        self.display_car()
        for elem_t in self.distance_prop:
            print(elem_t)
        print()
        print(self.display_load_all_axles(self.distance_prop))

    def display_car(self):
        #
        print("{} осей в машине".format(len(self.axle_in_car)))
        self.display_axles_in_car()

    def display_axles_in_car(self):
        #
        for elem in self.axle_in_car:
            print(elem)
        print()

    def display_load_all_axles(self, temp_list) -> None:
        """
        Выводит максимальную нагрузку осей на мост за время проезда по мосту

        :return: None
        """
        print(self.sum_load(temp_list))

    def set_list_travel(self, *args) -> list[Any]:
        """
        Собирает список значений нагрузок на мост под каждой из осей, находящейся на мосту
#
        :return: list
        """
        temp_travel = list()
        if args:
            #
            prop = int((args[0] + args[1]) / 2)
            for way in range(int((-1) * self.len_bridge / 2), int(self.len_bridge / 2) + 1, 1):  # step 1
                temp_list = list()
                for axle in self.axle_in_car:
                    if way - axle.axle in range(self.len_way - prop + 1):
                        temp_list.append(*axle.distance_traveled_prop(self.len_way, way - axle.axle))
                    else:
                        temp_list.append([0, 0, 0])  # исправить

                temp_travel.append(temp_list)
        else:
            #
            for way in range(int((-1) * self.len_bridge / 2), int(self.len_bridge / 2) + 1, 1):  # step 1
                temp_list = list()
                for axle in self.axle_in_car:
                    if way - axle.axle in range(int((-1) * self.len_way / 2), int(self.len_way / 2)):
                        temp_list.append(*axle.distance_traveled(self.len_way, way - axle.axle))
                    else:
                        temp_list.append([int(way - axle.axle + self.len_way / 2), 0, 0])

                temp_travel.append(temp_list)
        return temp_travel

    @classmethod
    def sum_load(cls, temp_list) -> list[Any]:
        """
        Возвращает список координат и нагрузок, отсортированные по максимальному значению суммы нагрузок осей на мост

        :return: list
        """
        sum_count = 0
        temp = None
        for elem in temp_list:
            temp_sum = 0
            for temp_elem in elem:
                temp_sum += temp_elem[2]
                if sum_count < temp_sum:
                    sum_count = temp_sum
                    temp = elem
        return [temp, round(sum_count, 3)]


class AxlesInTheBridge:
    """
    Имитация оси машины, и её давления на точку опоры

    """

    def __init__(self, num_axle, *args) -> None:
        self.angle = 0.5
        self.axle = args[0][0]
        self.load = args[0][1]
        self.num_axle = num_axle

    def __str__(self) -> str:
        """
        Возвращает текст с номером оси, расстоянием от первой оси, нагрузку оси на опору

        :return: str
        """
        return 'Номер оси:{number}. Расстояние от начала первой оси {axle} метров, нагрузка: {load} тонн'. \
            format(number=self.num_axle,
                   axle=self.axle,
                   load=self.load
                   )

    def __eq__(self, other):
        return self.axle is other.axle

    def __ne__(self, other):
        return self.axle is not other.axle

    def __lt__(self, other):
        """
        Производим сравнение < по удаленности осей от первой оси
        """
        return self.axle < other.axle

    def __gt__(self, other):
        """
        Производим сравнение > по удаленности осей от первой оси
        """
        return self.axle > other.axle

    def get_load(self, ordinate: float) -> float:
        """
        Возвращает нагрузку оси на заданную точку моста

        :param way: int
        :return: float
        """
        return round(ordinate * self.load / 100, 3)

    def distance_traveled(self, len_bridge: int, way: int) -> list[Any]:
        """
        Возвращает нагрузку моста в точке нахождения оси

        :param len_bridge: int
        :param way: int
        :return: list
        """
        temp = list()
        temp.append(
            [
                way + int(len_bridge / 2),
                abs(abs(way) * self.angle - len_bridge / 4) / 100,
                self.get_load(abs((abs(way)) * self.angle - len_bridge / 4))
            ]
        )
        return temp

    def distance_traveled_prop(self, len_bridge: int, way: int):
        #
        temp = list()
        temp.append(
            [
                way,
                round(way / len_bridge, 3),
                self.get_load(way / len_bridge)
            ]
        )  # установить значение угла
        return temp


if __name__ == "__main__":
    # car_axle_list = [0, 175, 405, 585, 795, 970, 1150, 1325]  # расстояния между осями
    # car_load_list = [15.35, 15.35, 15.35, 15.35, 15.35, 15.35, 15.35, 15.35]
    car_axle_list = [0 ]  # расстояния между осями
    car_load_list = [15.35]
    car = MachineWithAxles(1050, car_axle_list, car_load_list, 100, 150)
    # car.display_info_load_bridge()
    # print()
    # car.display_load_all_axles()
    print()
    car.display_info_load_prop()
    print(car)
