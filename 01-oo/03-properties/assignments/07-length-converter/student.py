class LengthConverter:
    def __init__(self):
        self.__meter = 0

    @property
    def meter(self):
        return self.__meter

    @meter.setter
    def meter(self, meter):
        self.__meter = meter

    @property
    def feet(self):
        return self.__meter * 3.28084

    @feet.setter
    def feet(self, feet):
        self.__meter = feet / 3.28084

    @property
    def inch(self):
        return self.__meter * 39.3701

    @inch.setter
    def inch(self, inch):
        self.__meter = inch / 39.3701

