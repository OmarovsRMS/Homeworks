from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def expend(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def expend(self):
        return self.size/6.5 + 0.5

class Suit(Clothes):
    def __init__(self, height):
        self.height = height
    @property
    def expend(self):
        return self.height*2 + 0.3

coat = Coat(20)
print(coat.expend)

suit = Suit(10)
print(suit.expend)

print(coat.expend + suit.expend)
