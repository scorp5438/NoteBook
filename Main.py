from NoteBook import NoteBook

if __name__ == "__main__":
    isWork = True
    while isWork:
        noteBook = NoteBook()
        noteBook.menu()
        work = input("Продолжить? y/n:\n")
        if work.lower() == 'y':
            isWork = True
        elif work.lower() == 'n':
            isWork = False
        else:
            print("Введена некорректная команда, завершение програмы")
            isWork = False
