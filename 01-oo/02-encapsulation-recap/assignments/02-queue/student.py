class Queue:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)
    
    def next(self):
        return_item = self.__items[0]
        self.__items.pop(0)
        return return_item
    
    def is_empty(self):
        return len(self.__items) == 0
    

