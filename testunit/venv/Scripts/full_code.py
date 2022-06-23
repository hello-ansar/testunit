
import random

class full_code():

    def Matrix(n, m):
        arr = [[random.randint(1, 10) for i in range(n)] for j in range(m)]
        return arr

    def func(arr, n, m):
        k = 0
        sum = 0
        for i in range(m):
            for j in range(n):
                sum += arr[j][i]
            for a in range(n):
                if(arr[a][i] > sum - arr[a][i]):
                    k += 1
            sum = 0
        return k

    def maximum(arr, n, m):
        sum = 0
        max = 0
        q = 0
        for i in range(m):
            for j in range(n):
                sum += arr[j][i]
            if(max < sum):
                q = i
                max = sum
        sum = 0
        return q

    def cout(arr, n):
        for i in range(n):
            print(arr[i])


if __name__ == "__main__":
    a = full_code
    arr = a.Matrix(4, 4)
    a.cout(arr, 4)
    print("Кол-во особых элементов матрицы: ", a.func(arr, 4, 4))
    print("Номер столбца с максимальной суммой всех элементов: ", a.maximum(arr, 4, 4))








