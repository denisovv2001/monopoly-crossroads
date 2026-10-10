import random

class Chattel:
    '''Базовый класс игровых клеток поля'''

    def __init__(self, price: int, color: str, title: str):
        '''
        Примеры параметров для имущества:
        150, (192, 192, 192), "Water warks"
        0, (169, 169, 169), "Go to jail"
        -100, (255, 192, 203), "Super tax pay $100"
        '''
        # Цена за недвижимость
        # <0 - Налоги, =0 - особое поле (GO, Jail), >0
        self.price = price
        # Цвет ячейки в RGB - кортеж (255, 0, 0)
        self.color = color
        # Текст имущества отображаемый на игровом поле
        self.title = title

    def __str__(self):
        """Вызывается, когда пытаются вывести объект как строку"""
        return f"Название: {self.title}, Цена:{self.price}, Цветовая группа: {self.color}"
    
    def on_land(self, player):
        """Вызывается, когда игрок наступает на клетку"""
        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
        print(f"Игрок {player.name} наступил на обычную клетку {self.title}")
    
    def status(self):
        '''Получение информации об экземпляре Chattle для пользователя'''
        #TODO Использовать __str__ и __repr__ вместо метода status в Chattel
        print(f"Название улицы - {self.title}\nСтоимость - ${self.price}\nЦветовая группа - rgb{self.color}\n")

    def get_title(self):
        '''Получение имени объекта Chattel'''
        return self.title


class StartCell(Chattel):
    '''Класс для поля GO'''

    def on_land(self, player):
        """Вызывается, когда игрок точно попал на GO"""
        # Игрок получает 400 при точном попадании на GO
        player.money += 400
        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
        print(f"{player.name} прошёл круг! Точное попадание на GO. Получено $400. Баланс: {player.money}$")


class TaxCell(Chattel):
    '''Класс для полей Tax'''

    def on_land(self, player):
        # Игрок платит налог
        player.money -= 200
        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
        print(f"{player.name} заплатил налог $200. Баланс: {player.money}$")


class Company(Chattel):
    '''Класс для Company'''
    
    def __init__(self, index, name, colorGrup, price, isBuy, neighbors=None):
        '''
        Пример параметров для компании
        12, "Electric company", (192, 192, 192), 150, False, [11, 13]
        '''
        # Игрок владеющий имущестом
        self.owner = "Bank"
        # Цена при покупки недвижимости у Банка
        self.price = 150
        #super().__init__(index, name, colorGrup, price, isBuy, propertyOwner, neighbors)

    def __str__(self):
        """Вызывается, для строкового представления объекта Company"""
        return f"Владелец компании {self.owner}, стоимость: {self.price}"

    def on_land(self, player, cube):
        """Вызываем при попадании игрока на компанию"""

        #Компания не наступившего игрока и не в банке
        if self.owner != player.name and self.owner != "Bank":
            # вычисление ренты за компанию
            summRent = self.rent(player=player,cube=cube)
            # уменьшение наличности игрока на сумму ренты
            player.money -= summRent
            #TODO не забыть добавить деньги на счёт владельца компании
            #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
            print(f"{player.name} наступил в компанию {self.name} принадлежащую {self.owner}. ")
            print(f"{player.name} заплатил аренду ${summRent}. Баланс: {self.name}$")
        #компания игрока
        elif self.owner == player.name:
            #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
            print(f"{player.name} наступил на свою компанию {self.name}")
        #Компания в банке
        elif self.owner == "Bank":
            #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
            print(f"Компанию {self.name} можно купить за ${self.price}")
            print(f"Введите y для покупки или n для отмены: ")
            # ввод команды с клавиатуры для покупки имущества
            command = str(input())
            # игрок хочет купить
            if command == "y":
                # у игрока есть деньги
                if self.price <= player.money:
                    # Уменьшаем сумму денег игрока на стоимость Компании
                    player.money -= self.price 
                    # Добавляем индекс Компании к имуществу игрока
                    player.add_property(self.index) 
                    # Говорим, что Компания приобретена
                    self.isBuy = True 
                    # задаём владельцем купленного имущества игрока
                    self.owner = player.name
                # денег не хватает
                else:
                    #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                    print(f"У игрока {player.name} недостаточно средств ({player.get_money()}) для покупки {self.name}")
                    #TODO Реализовать возможность закладывать имущество у государства во время покупки
            # игрок отказывается от имущества
            elif command == "n":
                #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                print(f"Компания {self.name} на аукционе")
                #TODO реализовать аукцион

    def get_count_of_user(self, player, color):
        """Получаем кол-во незаложенных компаний игрока"""
        pass
        #TODO Возвращать число Компаний данной цветовой группы у владельца
        # Есди цвет одинаковый у двух индексов, то лни в одной Монополии
        # count = 0
        # 
        # if self.isBuy:
        #     for index in player.property:
        #         if self.colorGrup == player.
        #           

    def rent(self, player, cube):
        """Вычисление и возврат суммы ренты за оплату 
        комунальных услуг. Учитывается кол-во незаложенных
        компаний у владельца"""
        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
        print(f"Игрок {player.name} должен уплатить ренту за посещение {self.name}")
        pass
        # return int

class Gamer:
    """Класс игрока"""
    
    def __init__(self, name: str, money: int, index: int):
        self.name = name
        self.money = money
        self.index = index # Индекс, где находится фишка

    def __str__(self):
        """красиво выводит объект Gamer в виде строки"""
        return f"Имя игрока:{self.name} Положение на карте:{self.index} Наличные:{self.money}"
    
    def get_index(self):
        """Получаем индекс ячейки, на которой стоит игрок"""
        return self.index

    def set_money(self):
        """Получение зарплаты при попадании или проходе через GO"""
        # Точное попадание на GO
        if self.index == 0:
            #TODO учесть попадание на GO по карточке (ЗП 200!)
            # Двойная зарплата при броске кубиков
            self.money += 400 
        else:
            # Проход через GO или попадание на GO по карточке
            self.money += 200

    def money_status(self):
        """выводим сумму наличных игрока"""
        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
        print(f"У игрока {self.name} есть {self.money}$")

    def set_index(self, index):
        """Перемещение игрока (его индекса) по карте"""
        #TODO Реализовать внутренний круг
        # Идёт в тюрьму
        if index == 30: 
            self.index = index
            #TODO Реализовать нахождение в тюрьме
        # проходим через "Go" (делаем круг)
        elif self.index + index > 39: 
            # Округляем значения индексов, чтобы не уйти за границы поля
            self.index = self.index + index - 40 
            # Получаем зарплату
            self.set_money() 
            # узнаём кол-во денег игрока после ЗП
            self.money_status()
        # обычное движение по большому кругу
        else:
            # перемещаемся с текущего индеса сразу на нужный
            self.index += index 

    def status(self):
        """общая информация игрока"""
        #TODO Использовать __str__ и __repr__ вместо метода status в Gamer
        print(f'Игрок "{self.name}", Находится на поле с индексом {self.index}')    

    def rollDice(self):
        """Бросок одного кубика 6/6"""
        return random.randint(1,6)

    def go(self):
        """Движение игрока по игровому полю"""
        # кол-во дублей за ход
        doubleCount = 0
        # Цикл хода игрока
        while True:
            # ввод команды с клавиатуры для броска кубиков при движении
            command = input("Введите t для броска кубиков: ")
            # игрок ввёл нужную команду для броска кубиков
            if command == 't':
                # число очков первого кубика
                val1 = self.rollDice()
                # число очков второго кубика
                val2 = self.rollDice()
                # сумма на костяшках
                sum1 = val1 + val2
                #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                print("\nВ",doubleCount+1, "бросок")
                print(f"У {self.name} выпало: {val1} {val2}")
                print("сумма очков: ",sum1)
                # выпал очередной дубль
                if val1 == val2:
                    # увеличиваем на 1 кол-во дублей в этом ходу игрока
                    doubleCount = doubleCount + 1
                    # текущий дубль не третий
                    if doubleCount < 3:
                        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                        print(doubleCount, "Дубль!", val1, val2)
                        self.set_index(sum1)
                        #TODO Использовать __str__ вместо метода status в Gamer
                        self.status()
                        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                        print("Делайте новый бросок.")
                    # игрок выкинул за ход три дубля
                    else:
                        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                        print("Третий дубрь подряд.")
                        print("Вы отправляетесь в тюрьму.")

                        # Передаём индекс клетки Идти в тюрьму
                        self.set_index(30) 

                        #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                        print("ход завершён")
                        print("############")

                        # Обнуляем кол-во дублей
                        doubleCount = 0

                        #TODO реализовать механику попадания игрока в тюрьму

                        # прерываем выполнение цикла хода игрока
                        break
                        # неожиданное завершение хода тюрьмой ?return -1
                # На костях выпали разные значения
                else:
                    # телепортируем игрока на нужную ячейку
                    self.set_index(sum1)
                    #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                    # выводим информацию о игроке в консоль
                    self.status()
                    print("ход завершён")
                    print("------------")
                    # Обнуляем кол-во дублей
                    doubleCount = 0
                    # выходим из цикла движения
                    break
                    # игрок штатно закончил движение ?return 0
            #TODO здесь можно обрабатывать и другие механики во время хода игрока (продажа имущества, сделки)

            # игрок ввёл неожиданную команду
            else:
                #TODO Возвращать f-строку и выводить в нужном месте, а не выводить внутри класса
                print("\nНеизвестная команда")


if __name__ == '__main__':
    print("Выполнено с помощью structs.py")
    cella = TaxCell(-100,(255,255,255),"Super Tax")
    cellb = Company(12, "Electric company", (192, 192, 192), 150, False, [11, 13])
    cellc = StartCell(0,(0,0,0), "GO")
    player = Gamer("Ivan", 700, 0)
    print(cella)
    print(cellb)
    print(cellc)
    print(player)

