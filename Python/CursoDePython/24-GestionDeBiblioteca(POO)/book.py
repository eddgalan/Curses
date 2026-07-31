class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'El libro "{self.title}" ha sido alquilado')
        else:
            print(f'El libro "{self.title}" no está disponible')

    def return_book(self):
        self.available = True
        print(f'El libro "{self.title}" ha sido devolvido')