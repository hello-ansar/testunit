import unittest

from full_code import full_code

class MyTestCase(unittest.TestCase):

    def test_func(self, arr = full_code.Matrix(4, 4), n = 4, m = 4):
        k = 0
        sum = 0

        for i in range(m):
            for j in range(n):
                sum += arr[j][i]
            for a in range(n):
                if(arr[a][i] > sum - arr[a][i]):
                    k += 1
            sum = 0

        a = full_code
        self.assertEqual(a.func(arr, n, m), k)





if __name__ == '__main__':

    unittest.main()
