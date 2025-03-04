class CircularBuffer:
    def __init__(self, buffer_size: int):
        self.__buffer = []
        self.buffer_limit = buffer_size

    def add(self, adding):
        self.__buffer.append(adding)
        if len(self.__buffer) > self.buffer_limit:
            self.__buffer.pop(0)

    @property
    def buffer(self):
        return self.__buffer

    def __len__(self):
        return len(self.__buffer)

    def __getitem__(self, index):
        return self.buffer[index]