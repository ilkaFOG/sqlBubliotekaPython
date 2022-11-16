import peewee


from Book import Book
from Library import Library
from ui import Ui
from State import StateManager, States


class App:
    @staticmethod
    def run():
        Ui.clear()

        library = Library()
        library.add(Book('asd',"asd",1111))
        state_manager = StateManager(library)
        state_manager.state_changed.add_listener(Ui.draw_ui)
        state_manager.change_state(States.Main)

        while state_manager.is_work:
            state_manager.current_state.handle_input(state_manager)


if __name__ == '__main__':
    try:

        library = Library()
        library.connect()
        library.add(Book('Первому игроку приготовится', 'Эрнест Клайн', 2001))

        print(library.count())
        print(library.get_at(1))
        print(library.get_all_books())

        library.close()

    except peewee.InternalError as px:
        print(str(px))            