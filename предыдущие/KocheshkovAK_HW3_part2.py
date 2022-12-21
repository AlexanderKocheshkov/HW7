x0, y0 = 0, 0 #Начальная позиция
x, y = 0, 0
going = "Играем"
while going != "СТОП":
    print("Куда идёт персонаж? Сколько шагов он пройдёт в этом направлении?")
    print("Напишите через пробел. Для выхода напишите 'СТОП'")
    str=input()
    if str == "СТОП":
        print("Спасибо за игру!")
        going = "СТОП"
    else:
        vec, steps = str.split(" ")
        steps = int(steps)
        if steps < 0:
            print("Ошибка! Нельзя сделать отрицательное количество шагов!")
        if steps == 0:
            print("Стоим на месте!")
        else:
            if vec == "Влево" or vec == "влево":
                x -= steps
                print("Персонаж сместился с ({0},{1}) в ({2}, {3})".format(x0, y0, x, y))
                x0 -=steps
            if vec == "Вправо" or vec == "вправо":
                x += steps
                print("Персонаж сместился с ({0},{1}) в ({2}, {3})".format(x0, y0, x, y))
                x0 +=steps
            if vec == "Вверх" or vec == "вверх":
                y += steps
                print("Персонаж сместился с ({0},{1}) в ({2}, {3})".format(x0, y0, x, y))
                y0 +=steps
            if vec == "Вниз" or vec == "вниз":
                y -= steps
                print("Персонаж сместился с ({0},{1}) в ({2}, {3})".format(x0, y0, x, y))
                y0 -=steps
