import client
import server
import unittest

class CalcTest(unittest.TestCase):
    def test_multipliers(self):
        """Тест функции разложения числа на простые множители."""
        self.assertEqual(server.multipliers(0), "0 = 0*1")
        self.assertEqual(server.multipliers(1234567890), "1234567890 = 2*1 + 3*2 + 5*1 + 3607*1 + 3803*1")

    def test_correct(self):
        """Тест функции проверки введеного пользователем числа на корректность."""
        self.assertEqual(client.correct(""), "")
        self.assertEqual(client.correct("12345678q"), "")
        self.assertEqual(client.correct("1234567890"), b'1234567890')

if __name__ == '__main__':
    unittest.main()




