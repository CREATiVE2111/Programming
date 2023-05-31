import V3D
# отлавливание ошибок/исключения; f-строки; декоратор; копия
try:
    cords1 = str(input('Введите координаты вектора через пробел: '))
    cords2 = str(input('Введите координаты второго вектора: '))
    chislo = int(input('Введите число: '))
    vector1 = V3D.vektr3D(cords1)
    vector2 = V3D.vektr3D(cords2)
except (ValueError, TypeError):
    print("Введено не допустимое значение")
except Exception:
    print("Не известная ошибка")
else:
    #vector3 = V3D.vektr2_0('3 4 5')
    print('\n','Сложение векторов', vector1 + vector2)
    print('Вычитание векторов', vector1 - vector2)
    print('Скалярное произведение', vector1 * vector2)
    print('Векторное произведение', vector1.vektrProizv(cords2))
    print('Умножение вектора на число', vector1 * chislo)
    print('Деление вектора на число', vector1 / chislo)
    print('Норма вектора', vector1.norma())
vector2d = vector1.__copy__('57 23 3')
print(f'У 2D вектора:\nКоордината X = {vector2d.corX}\nКоордината Y = {vector2d.corY}\nКоордината Z = {vector2d.corZ}')