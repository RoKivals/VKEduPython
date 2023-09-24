class TicTacGame:
    def __init__(self):
        self.size = 3
        self.field = [[" " for _ in range(self.size)] for _ in range(self.size)]

    @staticmethod
    def main_menu():
        print("Добро пожаловать в игру \"Крестики-Нолики\"")
        print()
        print("Введите, чтобы выбрать действие")
        print('''
        1. Играть
        2. Настройки
        3. Выйти
        ''')

    @staticmethod
    def settings_menu():
        pass

    def show_board():
        pass

    def validate_input():
        pass

    def start_game():
        pass

    def check_winner():
        pass


if __name__ == "__main__":
    game = TicTac()
    game.start_game()
