class Player:
    def __init__(self, name, symbol):
        self.name = name
        self._symbol = symbol

    def __repr__(self):
        return self.name

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, val):
        if val not in ['X', 'O']:
            raise ValueError("Только X или O")
        self._symbol = val