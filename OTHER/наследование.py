class Human:
    def __init__(self, name, surname, age, post):
        self.name = name
        self.surname = surname
        self.age = age
        self.post = post



class Student(Human):
    def __init__(self, group, name, surname, age, post):
        super().__init__(name, surname, age, post)
        self.group = group


st1 = Student("отеле Элеон", "Огузок", "Лавров", 28, "шеф-поваром")
print(f"{st1.name} {st1.surname} стал {st1.post} в {st1.group} в {st1.age} лет")