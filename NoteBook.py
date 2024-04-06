from FileManager import FileManager
from Note import Note
import os
import datetime


class NoteBook:
    find_list = []

    @staticmethod
    def check_file():
        if not os.path.isfile("NoteBook.csv"):
            FileManager().write()
        slist_notes = FileManager().read()
        return slist_notes

    list_notes = check_file()

    def create_note(self, title, text):
        id_note = len(self.list_notes)
        note = Note(id_note, title, text)
        self.list_notes.append([i for i in (str(note)).split(';')])
        FileManager().write(self.list_notes)
        print(f"Заметка {note} добавлена")

    def show_notes(self):
        if os.path.isfile("NoteBook.csv"):
            self.list_notes = FileManager().read()
            for note in self.list_notes:
                # print(note)
                print(f"{note[0]:_<3}|{note[1]:_<25}|{note[2]:_<30}|{note[3]}")
        else:
            print("Файл не найден")

    def find_note(self, find_by, data):
        if os.path.isfile("NoteBook.csv"):
            self.list_notes = FileManager.read()
        else:
            return None
        for note in self.list_notes:
            if note[find_by].startswith(data):
                self.find_list.append(note)
        return self.find_list

    def edit_note(self, changes, title):
        d_t = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if not os.path.isfile("NoteBook.csv"):
            self.list_notes = FileManager().read()
        changes_list = self.find_note(1, title)
        changes_note = None
        if changes == "1":
            data = "Заголовок"
        else:
            data = "текст"
        if len(changes_list) > 1:
            print(self.list_notes[0])
            print(*changes_list, sep="\n")
            id_note = input("Найдено несколько заметок, введите id заметки, которую необходимо изменить:\n")
            for note in changes_list:
                if note[0] == id_note:
                    changes_note = note
            if changes_note is None:
                print("id не найден...")
            for index in range(len(self.list_notes)):
                if self.list_notes[index] == changes_note:
                    new_data = input(f"Введите новый {data}\n")
                    print(f"Заметка: {self.list_notes[index]} изменена, {data} заменен, на {new_data}")
                    self.list_notes[index][int(changes)] = new_data
                    self.list_notes[index][3] = d_t

        elif len(changes_list) == 1:
            new_data = input(f"Введите новый {data}\n")
            change_index = self.list_notes.index(changes_list[0])
            print(f"Заметка: {self.list_notes[change_index]} изменена, {data} заменен, на {new_data}")
            self.list_notes[change_index][int(changes)] = new_data
            self.list_notes[change_index][3] = d_t
        FileManager.write(self.list_notes)
        changes_list.clear()

    def delete_note(self, title):
        delete_list = self.find_note(1, title)
        delete_note = None
        if len(delete_list) > 1:
            print(self.list_notes[0])
            print(*delete_list, sep="\n")
            id_note = input("Найдено несколько заметок, введите id заметки, которую необходимо удалить:\n")
            for note in delete_list:
                if note[0] == id_note:
                    delete_note = note
            if delete_note is None:
                print("id не найден")
            for index in range(len(self.list_notes)):
                if self.list_notes[index] == delete_note:
                    delit = self.list_notes.pop(index)
                    print(f"Заметка: {delit} удалена")
                    break
        elif len(delete_list) == 1:
            self.list_notes.remove(delete_list[0])
            print(f"Заметка: {delete_list[0]} удалена")
        FileManager.write(self.list_notes)
        delete_list.clear()

    def menu(self):
        action = input(
            "Выберите действие:\n1 Создать заметку\n2 Показать список заметок\n3 Найти заметку\n4 Изменить заметку\n5 "
            "Удалить заметку\n")
        if action == "1":
            title = input("Введите заголовок заметки:\n")
            text = input("Введите текст заметки:\n")
            self.create_note(title, text)
        if action == "2":
            self.show_notes()
        if action == "3":
            res = []
            find_setting = input("По какому параметру искать?\n1 По заголовку\n2 По дате\n")
            if find_setting == "1":
                title = input("Введите искомый заголовок:\n")
                res = self.find_note(1, title)
            if find_setting == "2":
                data = input("Введите дату заметки в формате dd-mm-yyyy:\n")
                res = self.find_note(3, data)
            elif not self.find_list:
                print("Файла нет или значение не найдено.")
            elif find_setting not in "12":
                print("Введена некорректная команда")
            print(*res, sep="\n")
        self.find_list.clear()
        if action == "4":
            title = input("Введите заголовок заметки, которую необходимо изменить:\n")
            changes = input("Что необходимо изменить\n1 Заголовок\n2 Содержание:\n")
            if changes == "1" or changes == "2":
                self.edit_note(changes, title)
            else:
                print("Введена некорректная команда")
        if action == "5":
            title = input("Введите искомый заголовок:\n")
            self.delete_note(title)
        elif action not in "12345":
            print("Введена некорректная команда")
