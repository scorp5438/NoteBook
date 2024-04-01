import datetime

class Note:
    dT = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __init__(self, id, title, text, dateTime=dT):
        self.id = id
        self.title = title
        self.text = text
        self.dateTime = dateTime

    def __str__(self):
        return f"{self.id};{self.title};{self.text};{self.dateTime}"



