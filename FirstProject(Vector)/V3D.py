import copy
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'Функция {func.__name__} выполнилась {wrapper.count} раз')
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


class vektr3D:
    @counter
    def __init__(self, cord):
        cor = delenie(cord)
        self.corX = cor[0]
        self.corY = cor[1]
        self.corZ = cor[2]

    @counter
    def __add__(self, vektor2):
        x = self.corX + vektor2.corX
        y = self.corY + vektor2.corY
        z = self.corZ + vektor2.corZ
        return x, y, z

    @counter
    def __sub__(self, vektor2):
        x = self.corX - vektor2.corX
        y = self.corY - vektor2.corY
        z = self.corZ - vektor2.corZ
        return x, y, z

    @counter
    def __mul__(self, vektor2):
        if type(vektor2) == vektr3D:
            x = self.corX * vektor2.corX
            y = self.corY * vektor2.corY
            z = self.corZ * vektor2.corZ
            scalproizvedenie = x + y + z
            return scalproizvedenie
        if type(vektor2) == int:
            x = self.corX * vektor2
            y = self.corY * vektor2
            z = self.corZ * vektor2
            return x, y, z

    @counter
    def __truediv__(self, chislo):
        x = self.corX / chislo
        y = self.corY / chislo
        z = self.corZ / chislo
        return x, y, z

    @counter
    def vektrProizv(self, vektor2):
        a = delenie(vektor2)
        i = (self.corY * a[2]) - (self.corZ * a[1])
        j = ((self.corX * a[2]) - (self.corZ * a[0])) * (-1)
        k = (self.corX * a[1]) - (self.corY * a[0])
        return i, j, k
    @counter
    def norma(self):
        norm = (self.corX**2 + self.corY**2 + self.corZ**2) ** (0.5)
        return norm

    def __copy__(self, cord):
        vektr2D = vektr3D(cord)
        vektr2D.corZ = "такой координаты нет"
        return vektr2D




@counter
def delenie(cord):
    cor = cord.split()
    corX = int(cor[0])
    corY = int(cor[1])
    corZ = int(cor[2])
    return corX, corY, corZ

class vektr2_0(vektr3D):
    def norma2(self):
        norm = (self.corX**2 + self.corY**2 + self.corZ**2) ** (0.5)
        return norm



if __name__ == "__main__":
    viktor1 = vektr3D('1 2 3')
    print(viktor1.norma())
    print((viktor1.corX))
    print(dir(viktor1))
    viktor2 = copy.copy(viktor1)
    print(dir(viktor2))
    '''тёхмерный вектор
    перегрузить оепраторы
    выводить +
    скалдывать
    вычитать
    скалярное произведение
    векторное произведение
    делить умножать на число
    брать норму вектора'''