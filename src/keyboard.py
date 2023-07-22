from src.item import Item
from src.keyboardmixin import KeyboardMixin


class Keyboard(Item, KeyboardMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
