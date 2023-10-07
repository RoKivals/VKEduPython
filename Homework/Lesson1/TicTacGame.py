import os
import sys
import random


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class TicTacGame:
    def __init__(self):
        self._size = 15
        self.field = [[" " for _ in range(self.size)] for _ in range(self.size)]

    def __repr__(self):
        fields_numbers = [str(i + 1) for i in range(self.size)]
        empty_space_in_corner = ' ' * (len(str(self.size)) + 1)
        table_str = ""
        table_str = table_str + empty_space_in_corner + " ".join(i for i in fields_numbers) + '\n'

        for i in range(self.size):
            table_str = table_str + f"{i + 1:>{len(str(self.size))}}"
            for j in range(self.size):
                table_str = table_str + ' ' + f"{self.field[i][j]:{' '}^{len(str(j + 1))}}"
            table_str = table_str + '\n'

        return table_str

    @staticmethod
    def finish():
        os.system('cls||clear')
        print("Спасибо за игру!")
        sys.exit(0)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size >= 3:
            self._size = new_size
        else:
            self._size = 3

    @staticmethod
    def show_main_menu():
        os.system('cls||clear')
        print("Добро пожаловать в игру \"Крестики-Нолики\"")
        print()
        print("Введите, чтобы выбрать действие")
        print('''
        1. Играть
        2. Настройки
        3. Выйти
        ''')

    @staticmethod
    def show_settings_menu():
        os.system('cls||clear')
        print("Введите, чтобы выбрать действие: ")
        print('''
                1. Изменить размеры поля
                2. Вернуться
        ''')

    @staticmethod
    def show_start_game_menu():
        os.system('cls||clear')
        print("Выберите режим, в котором хотите играть")
        print("1. Два игрока")
        print("2. Против ПК (Бета версия)")
        print("3. Вернуться")

    def main_menu(self):
        flag = True
        while flag:
            self.show_main_menu()
            choice = input().strip()
            if choice == '1':
                self.start_game_menu()
                continue
            elif choice == '2':
                self.setting_menu()
                continue
            elif choice == '3' or choice == 'quit':
                self.finish()
                flag = False
            else:
                print("Такого варианта нет, попробуйте заново:")

    def setting_menu(self):
        flag = True
        while flag:
            self.show_settings_menu()
            choice = input().strip()
            if choice == '1':
                self.change_size()
                flag = False
            elif choice == '2':
                break
            else:
                print("Такого варианта нет, попробуйте заново:")

    def start_game_menu(self):
        flag = True
        while flag:
            self.show_start_game_menu()
            choice = input().strip()
            if choice == '1':
                self.start_game_vs_user()
                flag = False
            elif choice == '2':
                pass
            elif choice == '3' or choice == 'quit':
                break
            else:
                print("Такого варианта нет, попробуйте заново:")

    @staticmethod
    def input_player_names(count):
        res = []

        if count > 2 or count <= 0:
            raise ValueError("В эту игру нельзя играть таким кол-вом игроков")
        for num in range(count):
            new_player = input(f"Введите имя {num + 1} игрока")
            new_symbol
        player_x = input("Введите имя первого игрока (играет крестиками): ")
        player_o = input("Введите имя второго игрока (играет ноликами): ")
        return Player(player_x, 'X'), Player(player_o, 'O')

    def choosing_order(self):
        first_step = random.randint(1000) % 2
        player_x, player_o = self.input_names()
        if first_step == 0:
            player_1 = player_x
            player_2 = player_o
        else:
            player_1 = player_o
            player_2 = player_x

        print(f"{player_1}, вы ходите первым")
        print()
        return player_1, player_2

    def start_game_vs_user(self):
        player_1, player_2 = self.choosing_order()
        count_steps = 0
        curr_player = None

        while True:
            if count_steps % 2 == 0:
                curr_player = player_1
            else:
                curr_player = player_2

            print(f"{curr_player}, ваша очередь делать ход")
            curr_row, curr_col = self.get_row_and_col()
            self.field[curr_row][curr_col] = curr_player.symbol
            self.check_win(curr_row, curr_col, curr_player)
            count_steps += 1

    def get_row_and_col(self):
        while True:
            try:
                row_number = int(input("Выберите номер строки: "))
                print()
                col_number = int(input("Выберите номер столбца: "))
                if (row_number >= self.size + 1 or row_number <= 0) or (col_number >= self.size + 1 or col_number <= 0):
                    print(f"Число должно быть в диапазоне от 1 до {self._size + 1}")
                    continue

                if not self.check_empty_cell(row_number, col_number):
                    print("Эта ячейка уже занята, выберите другую")
                    continue

            except ValueError:
                os.system('cls||clear')
                print("Необходимо ввести число!")
            else:
                return row_number, col_number

    def check_empty_cell(self, row, col):
        return self.field[row][col] == ' '

    def check_win(self, row, col, player):
        symbol = player.symbol
        # check main diag
        if row == col:
            for i in range(self.size):
                if self.field[i][i] != symbol:
                    break
            else:
                print(f"{player.name} - Победитель!")
                input("Нажмите любую клавишу, чтобы закончить игру!")
                sys.exit(0)

        # check side diag
        elif row == abs(self.size - col - 1):
            for i in range(self.size):
                for j in range(self.size):
                    if self.field[i][j] != symbol and i == self.size - j - 1:
                        break
                else:
                    print(f"{player.name} - Победитель!")
                    input("Нажмите любую клавишу, чтобы закончить игру!")
                    sys.exit(0)

        else:
            # check vertical
            j = col
            for i in range(self.size):
                if self.field[i][j] != symbol:
                    break
            else:
                print(f"{player.name} - Победитель!")
                input("Нажмите любую клавишу, чтобы закончить игру!")
                sys.exit(0)

            # check horizontal
            i = row
            for j in range(self.size):
                if self.field[i][j] != symbol:
                    break
            else:
                print(f"{player.name} - Победитель!")
                input("Нажмите любую клавишу, чтобы закончить игру!")
                sys.exit(0)

    def change_size(self):
        print("Укажите размер нового поля: ")
        while True:
            try:
                new_size = int(input())
                self.size = new_size
                break
            except ValueError:
                print("Вам следует ввести число")

    @size.setter
    def size(self, value):
        self._size = value


if __name__ == "__main__":
    game = TicTacGame()
    game.main_menu()
