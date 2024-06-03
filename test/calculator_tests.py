from unittest import TestCase, main
from Chapter_one.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('4-2'), 2)

    def test_multi(self):
        self.assertEqual(calculator('3*3'), 9)

    def test_div(self):
        self.assertEqual(calculator('10/5'), 2.0)

    def test_no_singn(self):
        with self.assertRaises(ValueError) as e:
            calculator('asdf')
        self.assertEqual('Выражение должно содержать знак (+-/*)', e.exception.args[0])

    def test_two_singn(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать два целых числа и один знак.', e.exception.args[0])

    def test_many_singn(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+12')
        self.assertEqual('Выражение должно содержать два целых числа и один знак.', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2+3.2')
        self.assertEqual('Выражение должно содержать два целых числа и один знак.', e.exception.args[0])

    def test_string(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+d')
        self.assertEqual('Выражение должно содержать два целых числа и один знак.', e.exception.args[0])


if __name__ == '__main__':
    main()
