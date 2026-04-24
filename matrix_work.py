import random
import sys
class Matrix:
    def __init__(self,elements):
        for i in elements:
            for j in i:
                if type(j) not in (int, float):
                    raise TypeError('среди элементы матрицы должны быть float или int')
        self._el = elements
        self._rows = len(elements)
        self._cols = len(elements[0])
        for i in self._el:
            if len(i) == self._cols:
                continue
            else:
                raise ValueError('разное кол-во элементов в строках')
#######################################################################
    @property
    def size(self):
        return [self._rows,self._cols]

    @property
    def el(self):
        return self._el

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols
 ####################################################
    def __str__(self):
        result = []
        for row in self._el:
            result.append(' '.join(str(x) for x in row))
        return '--matrix--\n'+('\n'.join(result))
 ######################################################
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'нельзя солжить Matrix и {type(other).__name__}')
        if self.size != other.size:
            raise ValueError(f'нельзя сложить матрицы разной размерности')
        res_el = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self._el[i][j] + other._el[i][j])
            res_el.append(row)
        return Matrix(res_el)
#######################################################
    def __mul__(self, other):
        res_el = []
        if type(other) not in (Matrix, int, float):
            raise TypeError(f'нельзя умножить матрицу на {type(other).__name__}')
        if type(other) != Matrix:
            res_el =[[j*5 for j in i]for i in self._el]
        elif self.cols != other.rows:
                raise ValueError(f'нельзя умножить матрицу {self.size} на {other.size}')
        else:
            res_el = [[sum([self._el[i][k]*other._el[k][j] \
                       for k in range(self._cols)]) \
                        for j in range(other._cols)]\
                            for i in range(self._rows)]
        return Matrix(res_el)
    def __rmul__(self, other): #для умножения если число слева от матрицы
        res_el = []
        if type(other) not in (int, float):
            raise TypeError(f'нельзя умножить {type(other).__name__} на матрицу')
        return self.__mul__(other)
#######################################################
    @staticmethod
    def rnd_matrix(size,low_el=-10,high_el=10):
        el = []
        for k in range(size):
            el.append([random.randint(low_el,high_el) for j in range(size)])
        return Matrix(el)
##############################################################
if __name__ != '__main__':
    sys.exit(0)

m = Matrix([[1,2,3],[4,5,6]])
print(m.el)
print(m.rows)
print(m.cols)
print(m.size)
print(m)
print('*'*40)
a = Matrix.rnd_matrix(3)
b = Matrix.rnd_matrix(3)
print(f'A{a}\nB{b}')
c = a+b
print(f'A+B{c}')
print(f'(A+B)*5{c*5}')
print(f'5*(A+B){5*c}')
a = Matrix([[3],[4],[2]])
b = Matrix([[5,-2,3]])
print(f'A--{a}')
print(f'B--{b}')
print(f'B*A--{b*a}')
print(f'A*B--{a*b}')
print(Matrix([[2,-1],[3,-2]])\
      *Matrix([[2,-1],[3,-2]])\
      *Matrix([[2,-1],[3,-2]])\
      *Matrix([[2,-1],[3,-2]]))
