class Student:
    def __init__(self, name = "Omaba", age = 18):
        self.name = name
        self.age = age
    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

oleg = Student("Oleg", 23)
print(oleg.get_info())