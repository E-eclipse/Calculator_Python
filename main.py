from web3 import Web3
from web3.middleware import geth_poa_middleware 
from contract_info import abi, address_contract
from art import tprint

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=address_contract, abi=abi)

accounts = w3.eth.accounts
authorized_account = None

def clear_screen():
    print("\033[H\033[J")


def get_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Выберите вариант: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input("Пожалуйста, выберите номер варианта: ")
    return int(choice)


def login():
    try:
        public_key = input("Введите публичный ключ: ")
        password  = input("Введите пароль: ")
        w3.geth.personal.unlock_account(public_key, password)
        print(f"Вы успешно вошли в аккаунт\n\n")
        print("\n----------------------------------------------------------\n\n")


        global authorized_account
        authorized_account = public_key

        return public_key
    except Exception as e:
        print(f"Ошибка авторизации {e}")
        return None


def registraition():
    try:
        while True:
            result = 0

            print("Регистрация")
            print("Условия к паролю:\n" +
                  "Пароль должен содержать не менее 12 символовn\n"
                  "Должна быть минимум одна ЗАГЛАВНАЯ буква\n" +
                  "Должна быть минимум одна СТРОЧНАЯ буква\n" +
                  "Должна быть минимум одна ЦИФРА\n" +
                  "Должен быть минимум один СПЕЦИАЛЬНЫЙ СИМВОЛ\n" +
                  'Пароль НЕ ДОЛЖЕН содержать простых комбинаций по типу "qwerty", "password", "123" и т.д.')

            password = input("Введите пароль: ")


            for i in range(len(password)):
                if password[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    result += 1
                    break

            for i in range(len(password)):
                if password[i] in "abcdefghijklmnopqrstuvwxyz":
                    result += 1
                    break

            for i in range(len(password)):
                if password[i] in "1234567890":
                    result += 1
                    break

            for i in range(len(password)):
                if password[i] in "!@#$%^&*()-_=+":
                    result += 1
                    break

            if len(password) >= 12:
                result += 1

            
            a = 0
            for item in ["qwerty", "pass", "123", "abc", "solidity", "321", "999", "888", "123456789", "777", "666", "555", "444", "333",
                         "222", "111", "000", "zxc", "dota"]:
                if item not in password.lower():
                    a += 1
                    if a == len(["qwerty", "pass", "123", "abc", "solidity", "321", "999", "888", "123456789", "777", "666", "555", "444", "333",
                         "222", "111", "000", "zxc", "dota"]):
                        result += 1


            if result == 6:
                break


        account = w3.geth.personal.new_account(password)
        print(f"\nАккаунт: {account} успешно создан")

        global authorized_account
        authorized_account = account

    except Exception as e:
        print(f"Ошибка регистрации: {e}")
        return None
    
    
def create_Estate():
    try:
        Estate_Size = int(input("Рамер недвижимости: "))
        Pos = input("Адрес недвижимости: ")
        print("Тип недвижимости: ")
        Estate_type = get_choice(["Дом", "Квартира", "Подвал"])
        contract.functions.createEstate(Pos, Estate_Size, Estate_type-1).transact({"from": authorized_account})
        print("Недвижимость создана успешно\n\n")
    except Exception as e:
        print(f"Ошибка создания недвижимости: {e}")

def create_Advertisement():
    try:
        Estate_ID = int(input("Введите id недвижимости: "))
        Ad_Price = int(input("Введите цену недвижимости: "))
        contract.functions.createAd(Estate_ID, Ad_Price).transact({'from': authorized_account})
        print("Объявление создано успешно")
    except Exception as e:
        print(f"Ошибка создания объявления: {e}")

def update_Estate_status():
    try:
        EstateID = int(input("Введите id недвижимости: "))
        print("Установите статус недвижимости: ")
        Status = get_choice(["Продано", "Продается"])
        if Status - 1 == 0:
            contract.functions.updateEstateStatus(EstateID, True).transact({'from': authorized_account}) #-----------
        else:
            contract.functions.updateEstateStatus(EstateID, False).transact({'from': authorized_account}) #-------------

    except Exception as e:
        print(f"Ошибка обновления статуса недвижимости: {e}")

def update_Advertisement_status():
    try:
        AdvertisementID = int(input("Введите id объявления: "))
        print("Установите статус объявления: ")
        Stasus = get_choice(["Активно", "Неактивно"])
        contract.functions.updateAdStatus(AdvertisementID, Stasus-1).transact({'from': authorized_account})     # ------------
        print("Успешное изменение статуса")
    except Exception as e:
        print(f"Ошибка обновления статуса объявления: {e}")

def Withdrow():
    try:
        amount = int(input("Введите сумму для вывода средств: "))
        contract.functions.withdraw(amount).transact({'from': authorized_account})
        print("Средства успешно выведены")
    except Exception as e:
        print(f"Ошибка вывода средств: {e}")

def get_SmartContract_balance():
    try:
        balance = contract.functions.getBalance().call({'from': authorized_account})                # --------------------------------
        print(f"Баланс на смарт-контракте: {balance}")
    except Exception as e:
        print(f"Ошибка получения баланса смарт-контракта: {e}")

def get_Account_balance():
    try:
        balance = w3.eth.get_balance(authorized_account)
        print(f"Баланс вашего аккаунта: {balance} wei") 
    except Exception as e:
        print(f"Ошибка получения баланса аккаунта: {e}")

def get_Estates():
    try:
        print("Доступная недвижимость:\n")
        estates = contract.functions.getEst().call()
        for estate in estates:
            print(f"id: {estate[5]}\nРазмер: {estate[0]}\nАдрес: {estate[1]}\nВладелец: {estate[2]}\n" +      # ------------
                  f"Тип: {estate[3]}\nАктивность: {estate[4]}")
            print("\n----------------------------------------------------------\n")
    except Exception as e:
        print(f"Ошибка получения информации о существующей недвижимости: {e}")

def get_Advertisements():
    try:
        print("Существующие объявления:\n")
        advertisements = contract.functions.getAds().call()
        for advertisement in advertisements:
            print(f"id объявления: {advertisement[5]}\nid недвижимости: {advertisement[3]}\nЦена: {advertisement[2]}\n" +      # ------------
                  f"Владелец: {advertisement[0]}\nПокупатель: {advertisement[1]}\nСтатус: {advertisement[6]}")
            print("\n----------------------------------------------------------\n")
    except Exception as e:
        print(f"Ошибка получения информации о существующих объявлениях: {e}")

def buy_Estate():
    try:
        idAd = int(input("Введите id объявления для покупки недвижимости: "))
        tx_hash = contract.functions.buyEstate(idAd).transact({'from': authorized_account})
        print(f"Транзакция успешно отправлена: {tx_hash.hex()}")

    except Exception as e:
        print(f"Ошибка покупки недвижимости: {e}")

def deposit():
    try:
        value = int(input("Введите сумму для пополнения: "))
        contract.functions.deposit().transact({'from': authorized_account, "value": value})
    except Exception as e:
        print(f"Ошибка депозита: {e}")


def main():
    while True:
        clear_screen()
        try:
            global authorized_account
            authorized_account = None
            
            clear_screen()
            tprint("Welcome", "rnd-xlarge")
            choice = get_choice(["Вход", "Регистрация", "Выход"])
            if choice == 1:
                login()
            elif choice == 2:
                registraition()
            elif choice == 3:
                clear_screen()
                tprint("Good\nluck", "rnd-xlarge")
                break

            if choice != 3 and authorized_account != None:
                while True:
                    choice_2 = get_choice(["Создать недвижимость", "Создать объявление", 
                                           "Изменить статус недвижимости", "Изменить статус объявления",
                                            "Купить недвижимость", "Вывод средств", "Получить информацию о доступных недвижимостях",
                                            "Получить информацию о доступных объявлениях",
                                            "Получить баланс смарт-контракта", 
                                            "Получить баланс аккаунта",
                                            "Пополнить баланс смарт-контракта",
                                            "Выйти из аккаунта\n"])
                    
                    if choice_2 == 1:
                        create_Estate()

                    elif choice_2 == 2:
                        create_Advertisement()

                    elif choice_2 == 3:
                        update_Estate_status()

                    elif choice_2 == 4:
                        update_Advertisement_status()

                    elif choice_2 == 5:
                        buy_Estate()

                    elif choice_2 == 6:
                        Withdrow()

                    elif choice_2 == 7:
                        get_Estates()

                    elif choice_2 == 8:
                        get_Advertisements()

                    elif choice_2 == 9:
                        get_SmartContract_balance()

                    elif choice_2 == 10:
                        get_Account_balance()

                    elif choice_2 == 11:
                        deposit()

                    elif choice_2 == 12:
                        break

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()