class Koshelek:
    
    def upBalance(self, money, howmany):
        if howmany > 0:
            money += howmany
            print(money)
        else:
            print("Введите корректную сумму")

        return money

    def downBalance(self, money, howmany):
        if money - howmany < 0:
            print("Недостаточно средств")
        elif howmany <= 0:
            print("Введите корректную сумму")
        else:
            money -= howmany
            print(money)

        return money

    def money(self, money):
        print(money)


kosh1 = Koshelek()
kosh2 = Koshelek()

kosh2.upBalance(1000, 200)
kosh1.downBalance(100, 10)

Koshelek.name = 10