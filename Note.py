import datetime


class Note:
    d_t = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __init__(self, id_note, title, text, date_time=d_t):
        self.id_note = id_note
        self.title = title
        self.text = text
        self.date_time = date_time

    def __str__(self):
        return f"{self.id_note};{self.title};{self.text};{self.date_time}"
