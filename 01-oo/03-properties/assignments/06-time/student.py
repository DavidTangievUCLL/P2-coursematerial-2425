# Write your code here
class Time:
    def __init__(self, hour, minute, second):
        
        
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    @property
    def hours(self):
        return self.__h

    @property
    def minutes(self):
        return self.__m

    @property
    def seconds(self):
        return self.__s

    @hours.setter
    def hours(self, hour):
        if hour < 0 or hour > 23:
            raise ValueError("e")
        if not (0 <= hour <= 23):
            raise ValueError("a")
        self.__h = hour

    @minutes.setter
    def minutes(self, minute):
        if not (0 <= minute <= 59):
            raise ValueError("a")
        self.__m = minute

    @seconds.setter
    def seconds(self, second):
        if not (0 <= second <= 59):
            raise ValueError("a")
        self.__s = second
