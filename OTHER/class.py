class CleverHouse:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.mode = "In_House"

    def on_attributes(self, gadget_name):
        if gadget_name in self.attributes:
            gadget_mode = self.attributes[gadget_name]
            if gadget_mode == "off":
                self.attributes[gadget_name] = "on"
                return self.attributes[gadget_name]
            elif gadget_mode == "on":
                return "Устройство уже включено"
            else:
                return "Ошибка"
        else:
            return "Такого элемента не существует"

    def off_attributes(self, gadget_name):
        if gadget_name in self.attributes:
            gadget_mode = self.attributes[gadget_name]
            if gadget_mode == "off":
                return "Устройство уже выключено"
            elif gadget_mode == "on":
                self.attributes[gadget_name] = "off"
                return self.attributes[gadget_name]
            else:
                return "Ошибка"
        else:
            return "Такого устройства не существует"

    def res_mode(self):
        if self.mode == "In_House":
            self.mode = "Not_In_House"
        elif self.mode == "Not_In_House":
            self.mode = "In_House"

        return self.mode
    
    def add_attribute(self):
        attr = input("Введите название устройства: ")
        if attr not in self.attributes:
            self.attributes[attr] = "off"
            return self.attributes
        else:
            print("Такое устройство уже есть")

    def del_attribute(self):
        attr = input("Введите название устройства: ")
        if attr in self.attributes:
            del self.attributes[attr]
            return self.attributes
        else:
            print("Такого элемента не существует")






first = CleverHouse("Умный дом", {"Шторы": "off", "Утюг": "on"})

print(first.on_attributes("Шторы"))
print(first.off_attributes("Утюг"))
print(first.res_mode())
print(first.add_attribute())
print(first.del_attribute())
