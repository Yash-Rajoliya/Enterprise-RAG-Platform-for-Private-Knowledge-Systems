class ShortTermMemory:

    def __init__(self):
        self.buffer = []

    def add(self, item):
        self.buffer.append(item)