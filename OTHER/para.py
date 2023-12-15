class Student:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if type(new_name) == str:
            self.__name = new_name.capitalize()
        else: 
            return "Имя должно быть строкой"
        
        return self.__name

st1 = Student("Игорев", "Игорь", 17)
# st1.set_surname = 12
print(st1.set_name("бИоЛОгИя"))