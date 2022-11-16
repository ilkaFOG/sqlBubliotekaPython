from Console import Console


class Command:
    def __init__(self, activ:Console, description:str):
        self.__activ = activ
        self.__description = description
    
    def __str__(self):
        return f'Введите \'{self.__action.value}\'- для {self.__description}'

    def to_string(self):
        return f'Введите \'{self.__action.value}\'- для {self.__description}'

    @property
    def activ(self):
        return self.__action