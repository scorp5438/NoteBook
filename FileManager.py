import csv

class FileManager:
    _header = [["id", "Заголовок", "Текст", "Дата создания"]]

    @staticmethod
    def write(data = _header):
        with open("NoteBook.csv", "w", encoding="cp1251", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data)

    @staticmethod
    def read():
        list_notes = []
        with open("NoteBook.csv", "r", encoding="cp1251") as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader:
                list_notes.append(i)
        return list_notes

