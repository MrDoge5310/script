import os
import json


def print_config(config):
    print("Текущие наcторйки:")
    for el in config:
        print(el, ":", config[el])
        print("-------------------")


path = os.path.abspath("config.json")

with open(path, 'r') as file:
    config = json.load(file)

print("Настройка конфигурации....\n")
print_config(config)

instr = """1 - изменить Api-ключ
2 - изменить secret-key
3 - изменить userNo
4 - изменить eth_advNo
5 - изменить btc_advNo
6 - изменить лимиты
7 - изменить зазор по BTC
8 - изменить зазор по ETH
9 - показать изменения
0 - выход
"""

print(instr)
choice = int(input("Введите операцию\n"))
while choice != 0:
    if choice == 1:
        data = input("Введите новый ключ API")
        config['api_Key'] = data
    elif choice == 2:
        data = input("Введите новый ключ Secret")
        config['api_Key'] = data
    elif choice == 3:
        data = input("Введите новый userNo")
        config['userNo'] = data
    elif choice == 4:
        try:
            data = int(input("Введите новый eth_advNo"))
            config['eth_advNo'] = data
        except:
            print('Неверно введены данные')
    elif choice == 5:
        try:
            data = int(input("Введите новый eth_btcNo"))
            config['btc_advNo'] = data
        except:
            print('Неверно введены данные')
    elif choice == 6:
        try:
            min_price = int(input("Введите минимальную сумму ордера"))
            max_price = int(input("Введите максимальную сумму ордера"))
            config['minSingleTransAmount'] = min_price
            config['maxSingleTransAmount'] = max_price
        except:
            print('Неверно введены данные')
    elif choice == 7:
        try:
            data = float(input("Введите новый зазор BTC"))
            config['min_clearance_btc'] = data
        except:
            print('Неверно введены данные')
    elif choice == 8:
        try:
            data = float(input("Введите новый зазор ETH"))
            config['min_clearance_eth'] = data
        except:
            print('Неверно введены данные')
    elif choice == 9:
        print_config(config)

    choice = int(input("Введите операцию\n"))

print("Настройки сохранены")
with open(path, 'w') as file:
    json.dump(config, file)
