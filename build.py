"""создаём все поля для игровой доски большого и малого круга
Поля создаются на основе базового класса Chattel
"""

from structs import Chattel

#создаём пустой список карточек игрового поля
indexMap = []

def setupGame():
    """Создание карточек игрового поля"""
    input("Нажмите любую клавишу для начала")
    #счётчик общего кол-ва игровых полей
    countSell = 0

    #Словарь, со всеми полями игрового поля (0-39 большой круг)
    d = {
    0:(0, (255, 255, 255), "collect $200 salary as you pass GO"),
    1:(60, (165, 42, 42), "Old kent road"),
    2:(400, (173, 255, 47), "Taxi  fiat"),
    3:(60, (165, 42, 42), "White chapel"),
    4:(-200, (255, 192, 203), "Income tax pay $200"),
    5:(200, (255, 127, 80), "Kings cross station british railwais"),
    6:(100, (0, 0, 255), "The angel islington"),
    7:(0, (47, 79, 79), "Chance?/Community chest<"),
    8:(100, (0, 0, 255), "Euston road"),
    9:(120, (0, 0, 255), "Pentonville road"),
    10:(0, (112, 128, 144), "In jail/Jast visiting"),
    11:(140, (128, 0, 128), "Pall mall"),
    12:(150, (192, 192, 192), "Electric company"),
    13:(140, (128, 0, 128), "White hall"),
    14:(160, (128, 0, 128), "Northumber land avenue"),
    15:(200, (255, 127, 80), "Marylebone station british railwais"),
    16:(180, (255, 0, 255), "Bow street"),
    17:(0, (47, 79, 79), "Chance?/Community chest<"),
    18:(180, (255, 0, 255), "Marlborough street"),
    19:(200, (255, 0, 255), "Vine street"),
    20:(0, (119, 136, 153), "Free parking"),
    21:(220, (255, 0, 0), "Strand"),
    22:(0, (47, 79, 79), "Chance?/Community chest<"),
    23:(220, (255, 0, 0), "Fleet street"),
    24:(240, (255, 0, 0), "Trafalgar square"),
    25:(200, (255, 127, 80), "Fenchurch station british railwais"),
    26:(260, (255, 255, 0), "Leicester square"),
    27:(260, (255, 255, 0), "Coventry street"),
    28:(150, (192, 192, 192), "Water warks"),
    29:(280, (255, 255, 0), "Piccadilly"),
    30:(0, (169, 169, 169), "Go to jail"),
    31:(300, (0, 128, 0), "Regent street"),
    32:(300, (0, 128, 0), "Oxford street"),
    33:(400, (173, 255, 47), "Taxi  mersedes"),
    34:(300, (0, 128, 0), "Bond street"),
    35:(200, (255, 127, 80), "Liverpool station british railwais"),
    36:(0, (47, 79, 79), "Chance?/Community chest<"),
    37:(500, (0, 0, 128), "Park lane"),
    38:(-100, (255, 192, 203), "Super tax pay $100"),
    39:(600, (0, 0, 128), "Mayfair"),
    40:(0, (0, 0, 0), "Middle rank"),
    41:(100, (0, 255, 0), "Casino national"),
    42:(200, (0, 255, 0), "Casino continental"),
    43:(300, (0, 255, 0), "Casino metropol"),
    44:(400, (0, 255, 0), "Trap"),
    45:(150, (192, 192, 192), "Gas england national"),
    46:(400, (173, 255, 47), "Taxi  ford"),
    47:(0, (0, 255, 255), "Railway tax"),
    48:(0, (0, 128, 128), "Social help office"),
    49:(0, (0, 0, 0), ""),
    50:(0, (0, 0, 0), ""),
    51:(0, (0, 0, 0), ""),
    52:(0, (0, 0, 0), "")
     }
    # забираем значения из словаря
    all_d = d.values() 
    # вывод всех значений словаря в одном списке
    print(all_d) 
    # цикл создаёт игровые ячейки
    for sell in all_d: 
        #считаем число созданных карт
        countSell+=1
        #создаём экземпляр карточки
        chart = Chattel(price=sell[0], color=sell[1], title=sell[2])
        #добавляем экземпляр карточки в схему листов карты всего игрового поля
        indexMap.append(chart)
 
    #Проверка создания карточек
    for chart in indexMap:
        chart.status() #TODO вызывать метод __repr__ вместо status
    print(f"Успешно создано {countSell} игровых полей")
    # Возвращаем список карточек игрового поля
    return indexMap 

if __name__ == "__main__":
    print("Выполнено с помощью build.py")
