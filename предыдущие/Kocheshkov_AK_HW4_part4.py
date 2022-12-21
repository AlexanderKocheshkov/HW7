class MansPocket(): #Самая вместительная вещь!
    def __init__(self, inventory = {}, carryweight = 0, maxweight = 70):
        """
        Making inventory with default:
            inventory = {} - stuffs
            carryweight = 0 - weight that hero is carryin rn
            maxweight = 70 - max weight
        """
        self.inventory = inventory #Инвентарь
        self.carryweight = carryweight #Вес на данный момент
        self.maxweight = maxweight #Максимальный переносимый вес

    def additem(self, item, weight): #Для добавления предмета в инвентарь
        """
        Adding item to inventory
        item - item we are going to put
        weight - item's weight
        """
        if ((self.carryweight < self.maxweight) and 
                ((self.carryweight + weight) <= self.maxweight)):
            self.inventory[item] = weight
            self.carryweight += weight
        else: #Не прошли проверку(
            return print("Больше не унести!")

    def delitem(self, item): #Для удаления предмета из инвентаря
        """
        Deliting item from inventory
        item - item we are going to throw out
        """
        if item in self.inventory:
            self.carryweight -= self.inventory[item]
            self.inventory.pop(item)
        else:
            return print("Нет такого предмета!")

    def printinventory(self): #Для красивого просмотра инвентаря
        """
        printing inventory
        """
        c = 1
        for key, value in self.inventory.items():
            print("{0}. {1} весом: {2}".format(c, key, value))
            c += 1

#Можно было сделать ещё класс с предметами, но зачем так страдать
gameitems = {
    "Утигатана": 5.5,
    "Реки крови": 6.5,
    "Лунная вуаль": 6.5,
    "Шлем из Страны тростника": 3.6,
    "Доспех из Страны тростника": 8.3,
    "Перчатки из Страны тростника": 2.8,
    "Поножи из Страны тростника": 5.1,
    "Фляга с чудесным снадобьем": 3,
    "Фляга багровых слёз": 10,
    "Фляга лазурных слёз": 6,
    "Костяной свисток": 10,
    "Шлем Рыжей Гривы": 7.5,
    "Львиный доспех Радана": 17.5,
    "Перчатки Радана": 5.8,
    "Поножи Радана": 10.8
}
#Для облегчения себе жизни (поздно сел за 4 задание) разделил ключи и значения на списки. (Как я понимаю, раньше стоило так делать хоть для соблюдения хоть какого-то порядка содержимого словарей.)
gameitemskeys = ["Утигатана","Реки крови","Лунная вуаль","Шлем из Страны тростника",
                "Доспех из Страны тростника", "Перчатки из Страны тростника",
                "Поножи из Страны тростника","Фляга с чудесным снадобьем",
                "Фляга багровых слёз","Фляга лазурных слёз",
                "Костяной свисток","Шлем Рыжей Гривы","Львиный доспех Радана",
                "Перчатки Радана","Поножи Радана"]

gameitemsvalues = [5.5, 6.5, 6.5, 3.6, 8.3, 2.8, 5.1, 3, 10, 6, 10, 7.5, 17.5, 5.8, 10.8]

def print_game_items(gameitems): #Чтобы сократить код. Печетаем список предметов
    """
        Printing game items
        gameitems - list of game items
    """
    n = 1
    for key, value in gameitems.items():
        print("{0}. {1} весом: {2}".format(n, key, value))
        n += 1

#Чтобы был какой-то старт
print("Выберите действие:") 
print("1. Создать перcонажа")
just_for_start = input() #Пустая переменная для старта
chel = MansPocket() #Создаём объект класса 

a = True
while a: #Чтобы повторять действия
    print("Выберите действие: ")
    print(" 1. Добавить предмет в инвентарь\n 2. Удалить предмет из инвентаря")
    print("3. Посмотреть инвентарь\n 4. Выход")
    req = int(input()) 
    if req == 1:
        print("Какой предмет добавить?")
        print_game_items(gameitems)
        ans = int(input())
        i, w = gameitemskeys[ans-1], gameitemsvalues[ans-1]
        chel.additem(i, w)
    if req == 2:
        print("Какой предмет удалить?")
        chel.printinventory()
        keylist = list(chel.inventory.keys()) #Для создания списка ключей. Для поиска по индексу.
        ans = int(input())
        i = keylist[ans-1]
        chel.delitem(i)
    if req == 3:
        c = 1
        chel.printinventory()
    if req == 4:
        a = False
