from ast import Index
from typing_extensions import Self
from unittest import result


class matrix(object):
    def __init__(self, value:list):
        self.value = value
        self.balance_matrix()

    def __div__(self, other):
        result = []
        
        # coming soom...

        return matrix(result)

    def __mul__(self, other):
        result = []

        if len(self.value[0]) != len(other.value):
            raise IndexError

        for i in range(len(self.value)):
            temp_row = []
            for j in range(len(other.value[0])):
                temp_row.append(0)
            result.append(temp_row.copy())
        
        for i in range(len(self.value)):
            for j in range(len(other.value[0])):
                for k in range(len(other.value)):
                    result[i][j] += self.value[i][k]*other.value[k][j]

        return matrix(result)

    def __add__(self, other):
        result = []

        for i in range(len(self.value)):
            temp_row = []
            for j in range(len(self.value[i])):
                temp_row.append(self.value[i][j]+other.value[i][j])
            result.append(temp_row.copy())

        return matrix(result)

    def __sub__(self, other):
        result = []

        for i in range(len(self.value)):
            temp_row = []
            for j in range(len(self.value[i])):
                temp_row.append(self.value[i][j]-other.value[i][j])
            result.append(temp_row.copy())

        return matrix(result)

    def balance_matrix(self):
        if type(self.value[0]) != type([0,0]):
            self.value = [self.value]

        max_row_len = 0
        col_len = len(self.value)

        for i in self.value:
            max_row_len = len(i) if max_row_len < len(i) else max_row_len

        for i in range(col_len):
            while len(self.value[i]) < max_row_len:
                self.value[i].append(0)
                print("bruh")

if __name__ == "__main__":        
    x = matrix([[10, 20, 30]])
    y = matrix([[10],
                [20],
                [30]])

    print((y*x).value, (x+x).value, (x-x).value)
