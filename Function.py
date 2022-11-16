from Book import Book

book1=Book("Первому игроку приготовиться", "Эрнест Клайн", 2001)
book2=Book("Колобок", "Народ", 1996)
book3=Book("Библия", "Кто-то", 1)
# x=input("Введите целое число для выполнения команды: ")

class Function(Book):
    

    def __init__(self,mass):
        self.mass=mass        

    def add(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: "))
        addbook=Book(title,author,year)
        self.mass.append(addbook)



x=int(input("Введите целое число для выполнения команды: "))

if x == 1:
    func = Function([book1,book2])
    func.add()
    print("clear","Теперь в библиотеке есть эти книги:")
    for i in func.mass:
        print(i)