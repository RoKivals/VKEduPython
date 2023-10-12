import os
import sys
import random
import names
import time


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
        print("Игра автоматически завершится через 15 секунд")
        time.sleep(15)
        sys.exit(0)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size < 3:
            raise ValueError("Размер поля должен быть больше 3")
        self._size = new_size

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
                os.system('cls||clear')
                self.start_game_vs_user()
                flag = False
            elif choice == '2':
                print("Как говорил Буянов, игра в стадии беты, поэтому ждите!")
                pass
            elif choice == '3' or choice == 'quit':
                break
            else:
                print("Такого варианта нет, попробуйте заново:")

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
            self.field[curr_row][curr_col] = curr_player.symbol
            print(self.field)

            if self.check_win(curr_row, curr_col, curr_player):
                print(f"{curr_player.name} - Победитель!")
                input("Нажмите любую клавишу, чтобы закончить игру!")
                sys.exit(0)

            count_steps += 1
            os.system('cls||clear')

    def get_row_and_col(self):
        while True:
            try:
                row_number = int(input("Выберите номер строки: "))
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
                for j in range(self.size):
                    if self.field[i][j] != symbol and i == self.size - j - 1:
                        break
                else:
                    result = True

        else:
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

    def change_size(self):
        while True:
            try:
                new_size = int(input("\nУкажите размер нового поля: "))
                self.size = new_size
            except ValueError:
                os.system('cls||clear')
                print("\nВам следует ввести число (больше 2)!")
            else:
                break


def main():
    game = TicTacGame()
    game.main_menu()


if __name__ == "__main__":
    main()
