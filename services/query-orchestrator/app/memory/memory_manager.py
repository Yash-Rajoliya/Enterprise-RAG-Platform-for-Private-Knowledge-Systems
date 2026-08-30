from .short_term import ShortTermMemory
from .long_term import LongTermMemory


class MemoryManager:

    def __init__(self):
        self.short = ShortTermMemory()
        self.long = LongTermMemory()