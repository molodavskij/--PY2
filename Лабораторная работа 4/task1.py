import doctest


class Solid:
    """
    Класс описывает некоторые характеристики твердого тела при комнатной температуре
    Данный клас - базовый, так как все т/т делятся на п/п, металлы и диэлектрики
    """
    def __init__(self, name: str, n: float, p: float, energy_gap: float):
        """
        :param name: Название или хим. формула материала
        :param n: Концентрация электронов в т/т
        :param p: Концентрация дырок в т/т
        :param energy_gap: Ширина запрещенной зоны [Эв]

        Пример:
        >>> ex1 = Solid("Ge", 2.4*10**13, 2.4*10**13, 0.72) # создаем экземпляр класса - материала Ge
        """
        self.name = name
        self.n = n
        self.p = p
        self.energy_gap = energy_gap

    def __str__(self):
        return f"Твердое тело {self.name}, n={self.n}, p={self.p}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, n={self.n!r}, {self.p!r}, {self.energy_gap!r})"

    def to_define_conductivity_type(self):
        """
        Метод определяет тип проводимости в материале
        :return: n, p или i

        Пример:
        >>> ex2 = Solid("Ge", 2.4*10**13, 2.4*10**13, 0.72) # создаем экземпляр класса - материала Ge
        >>> ex2.to_define_conductivity_type()
        """
        ...

    @staticmethod
    def to_find_resistance(p_mobility: float, n_mobility: float, n: float, p: float):
        """
        Позволяет рассчитать удельное сопротивление материала
        1. Реальные значения не для п/п могут сильно отличаться
        2. Однако иногда теоритическая прикидка может быть полезна

        :param p_mobility: Подвижность дырок в материале
        :param n_mobility: Подвижность электроново в материале
        :param n: Концентрация электронов
        :param p: Концентрация дырок
        :return: Значение подвижности

        Пример:
        >>> Solid.to_find_resistance(1900.0, 3900.0, 2.4*10**13, 2.4*10**13)
        """
        ...


class Dielectric(Solid):
    """
    Класс описывает некоторые характеристики диэлектриков
    """
    def __init__(self, name: str, n: float, p: float, energy_gap: float, d: float):
        """
        :param name: Название или хим. формула материала
        :param n: Концентрация электронов в т/т
        :param p: Концентрация дырок в т/т
        :param energy_gap: Ширина запрещенной зоны [Эв]
        :param d: Диэлектрическая проницаемость среды

        Пример:
        >>> ex1 = Dielectric("SiO2", 2.4*10**13, 2.4*10**13, 0.72, 7) # создаем экземпляр класса - материала стекло
        """
        super().__init__(name=name, n=n, p=p, energy_gap=energy_gap)
        self.d = d

    def to_define_conductivity_type(self):
        """
        Перегружаем метод так как в диэлектриках приемущественно ионный механизм проводимости
        :return: ионный тип проводимости
        """
        print(f"{self.name} имеет ионный тип проводимости")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, n={self.n!r}, p={self.p!r}, " \
               f"energy_gap={self.energy_gap!r}, d={self.d})"


class Semiconductor(Solid):
    """
    Класс описывает некоторые характеристики полупроводника
    """
    def __init__(self, name: str, n: float, p: float, energy_gap: float):
        super().__init__(name=name, n=n, p=p, energy_gap=energy_gap)


if __name__ == "__main__":
    doctest.testmod()
