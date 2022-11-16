from Command import Command
from Console import Console
from ui import Ui
from Event import Event
from Library import Library


class State:
    def __init__(self, header:str, command_list):
        self.__header = header
        self.__command_list = command_list

    def __str__(self):
        string_command_list = ''

        for command in self.__command_list:
            string_command_list += command.to_string() + '\n'

        return f'{self.__header}\n{string_command_list}'

    def to_string(self):
        string_command_list = ''

        for command in self.__command_list:
            string_command_list += command.to_string() + '\n'

        return f'{self.__header}\n{string_command_list}'

class MainState(State):
    def handle_input(self, state_manager):
        user_input = Ui.get_int()
        if user_input == Console.Exit.value:
            print('Exit')
        elif user_input == Console.AddBook.value:
            print('AddBook')
        elif user_input == Console.RemoveBook.value:
            print('RemoveBook')
        elif user_input == Console.FindBook.value:
            print('FindBook')
        elif user_input == Console.PrintAt.value:
            print('PrintAt')
        elif user_input == Console.PrintAll.value:
            state_manager.change_state(States.PrintAll)
        else:
            pass # TODO

class PrintAllState(State):
    def handle_input(self, state_manager):
        book_list = ''
        library = state_manager.library.get_all()
        index = 1
        for book in library:
            book_list += f'{index} - {book}\n'
            index += 1
        Ui.draw_ui(book_list)
        Ui.get_sting()
        Ui.clear()
        state_manager.change_state(States.Main)


class StateManager:
    def __init__(self, library: Library):
        self.state_changed = Event()
        self.__current_state = States.Main
        self.library = library
        self.is_work = True

    @property
    def current_state(self):
        return self.__current_state

    def change_state(self, state: State):
        self.__current_state = state
        Ui.clear()
        # Выход для динамики - переписал шаблон с регулярным выражением
        string_state = self.__current_state.to_string() % self.library.count
        self.state_changed.invoke(string_state)


class States:
    Main = MainState(f'Сейчас в библиотеке %s книг.', [
        Command(Console.Exit, "выхода"),
        Command(Console.AddBook, "добавления книги"),
        Command(Console.RemoveBook, "удаления книги"),
        Command(Console.FindBook, "поиска книги"),
        Command(Console.PrintAt, "вывода детальной информации о книге"),
        Command(Console.PrintAll, "вывода всех книг")
    ])

    AddBook = State(f'Сейчас в библиотеке %s книг.', [
        Command(Console.Exit, "выхода"),
        Command(Console.Undo, "отмены"),
    ])

    RemoveBook = State(f'Сейчас в библиотеке %s книг.', [
        Command(Console.Exit, "выхода"),
        Command(Console.Undo, "отмены"),
    ])

    PrintAll = PrintAllState(f'Сейчас в библиотеке %s книг.', [
        Command(Console.Return, "отмены")
    ])