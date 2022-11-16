import os


class Ui:
    def draw_ui(strings_ui:str):
        print(strings_ui)

    def clear():
        clear_console = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        clear_console()

    def get_int():
        user_input = None
        while True:
            try:
                user_input = int(input('Ведите целочисленое число.\n'))
                return user_input
            except:
                print(f'{user_input}- не целочисленное число!')

    def get_string():
        user_input = None
        while True:
            try:
                user_input = str(input('Введите строку число.\n'))
                return user_input
            except Exception as e:
                print(e)