import os
import sys
import random
import time

import names
from player import *


class CustomException(ValueError):
    pass


class TicTacGame:
    def __init__(self):
        self._size = 3
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
        print("Спасибо за игру!\n")
        print("Игра автоматически завершится через 10 секунд")
        time.sleep(10)
        sys.exit(0)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size < 3:
            raise CustomException("Размер поля должен быть больше 3")
        self._size = new_size

    @staticmethod
    def show_main_menu():
        os.system("cls||clear")
        print('''
Добро пожаловать в игру \"Крестики-Нолики\"
        
Введите, чтобы выбрать действие:
        1. Играть
        2. Настройки
        3. Выйти
        ''')

    @staticmethod
    def show_settings_menu():
        os.system("cls||clear")
        print('''
Введите, чтобы выбрать действие: 
                1. Изменить размеры поля
                2. Вернуться
        ''')

    @staticmethod
    def show_start_game_menu():
        os.system("cls||clear")
        print('''
Выберите режим, в котором хотите играть
        1. Два игрока
        2. Против ПК (Бета версия)
        3. Вернуться
        ''')

    @staticmethod
    def get_state_main_menu():
        while True:
            result = input().strip()
            if result == '1':
                result = 1
                break
            elif result == '2':
                result = 2
                break
            elif result in {'3', 'quit'}:
                result = 3
                break
            else:
                print("Такого варианта нет, попробуйте заново:")
        return result

    def main_menu(self):
        self.show_main_menu()
        new_state = self.get_state_main_menu()
        return new_state

    @staticmethod
    def get_state_setting():
        while True:
            result = input().strip()
            if result == '1':
                result = 4
                break
            elif result == '2':
                result = 0
                break
            else:
                print("Такого варианта нет, попробуйте заново:")
        return result

    def get_input_size(self):
        while True:
            new_size = input("\nУкажите размер нового поля: ")
            try:
                new_size = int(new_size)
                self.size = new_size

            except CustomException:
                os.system('cls||clear')
                print("\nВам следует ввести число, которое больше 2!")

            except ValueError:
                os.system('cls||clear')
                print("\nВам следует ввести число!")

            else:
                return 2  # setting_menu()

    def change_size(self):
        new_state = self.get_input_size()
        return new_state

    def setting_menu(self):
        self.show_settings_menu()
        new_state = self.get_state_setting()
        return new_state

    @staticmethod
    def get_state_game_menu():
        while True:
            choice = input().strip()
            if choice == '1':
                os.system('cls||clear')
                choice = 5
                break
            elif choice == '2':
                print("Как говорил Буянов, игра в стадии беты, поэтому ждите!")
                choice = 1
                break
            elif choice in {'3', 'quit'}:
                choice = 0
                break
            else:
                print("Такого варианта нет, попробуйте заново:")
        return choice

    def start_game_menu(self):
        self.show_start_game_menu()
        new_state = self.get_state_game_menu()
        return new_state

    @staticmethod
    def input_player_names():
        player_x = input("Введите имя первого игрока (играет крестиками): ")
        player_o = input("Введите имя второго игрока (играет ноликами): ")
        return Player(player_x, 'X'), Player(player_o, 'O')

    @staticmethod
    def input_player_vs_pc_name():
        symbols = ['X', 'O']
        player_user = input("Введите своё имя: ")

        while True:
            symbol_user = input("Выберите ваш символ [X / O]: ")
            if symbol_user not in symbols:
                print("Такой символ недоступен.")
                continue
            symbols.remove(symbol_user)

        player_pc = names.get_first_name(gender='male')
        print(f"Вашего соперника зовут: {player_pc}")
        return Player(player_user, symbol_user), Player(player_pc, *symbols)

    def choosing_order(self):
        first_step = random.randint(0, 1000) % 2
        player_x, player_o = self.input_player_names()
        if first_step == 0:
            player_1 = player_x
            player_2 = player_o
        else:
            player_1 = player_o
            player_2 = player_x

        print(f"\n{player_1}, вы ходите первым\n")

        input("Нажмите Enter, чтобы продолжить")
        return player_1, player_2

    def get_row_and_col(self):
        while True:
            try:
                row_number = int(input("Выберите номер строки: "))
                col_number = int(input("Выберите номер столбца: "))
                if ((row_number >= self.size + 1 or row_number <= 0)
                        or (col_number >= self.size + 1 or col_number <= 0)):
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
        result = False
        symbol = player.symbol
        # check main diag
        if row == col:
            for i in range(self.size):
                if self.field[i][i] != symbol:
                    break
            else:
                result = True

        # check side diag
        elif row == abs(self.size - col - 1):
            for i in range(self.size):
                j = self.size - i - 1
                if self.field[i][j] != symbol:
                    break
            else:
                result = True

        # check vertical
        j = col
        for i in range(self.size):
            if self.field[i][j] != symbol:
                break
        else:
            result = True

        # check horizontal
        i = row
        for j in range(self.size):
            if self.field[i][j] != symbol:
                break
        else:
            result = True

        return result

    def start_game_vs_user(self):
        player_1, player_2 = self.choosing_order()
        count_steps = 0

        while True:
            if count_steps % 2 == 0:
                curr_player = player_1
            else:
                curr_player = player_2

            print(self)
            print(f"{curr_player}, ваша очередь делать ход")
            curr_row, curr_col = self.get_row_and_col()
            self.field[curr_row - 1][curr_col - 1] = curr_player.symbol
            print(self.field)

            if self.check_win(curr_row, curr_col, curr_player):
                print(f"{curr_player.name} - Победитель!")
                input("Нажмите любую клавишу, чтобы закончить игру!")
                sys.exit(0)

            count_steps += 1
            os.system('cls||clear')


def main():
    game = TicTacGame()
    state = 0
    while True:
        if state == 0:
            state = game.main_menu()
        elif state == 1:
            state = game.start_game_menu()
        elif state == 2:
            state = game.setting_menu()
        elif state == 3:
            game.finish()
        elif state == 4:
            state = game.change_size()
        elif state == 5:
            game.start_game_vs_user()


if __name__ == "__main__":
    main()
