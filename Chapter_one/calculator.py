def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)

            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать два целых числа и один знак.')


if __name__ == '__main__':
    print(calculator('2*2'))
