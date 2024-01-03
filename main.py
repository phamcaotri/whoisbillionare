from typing import *

class Estate:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} {self.price}"