import string


def password_str(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak!'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
        continue
    if count == 3:
        return 'Very Good!'
    return 'Weak!' if count == 1 else 'Good!'

    # if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
    #     return 'Weak!'
    # if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
    #     return 'Very Good!'
    # if (any(e in digits for e in value) and (e in lowers for e in value)) or (
    #          any(e in digits for e in value) and (e in uppers for e in value)) or (
    #          any(e in lowers for e in value) and (e in uppers for e in value)):
    # return 'Good!'

if __name__ == '__main__':
    assert password_str('') == ('Too Weak!')
    assert password_str('1234567') == ('Too Weak!')
    assert password_str('asdfghj') == ('Too Weak!')
    assert password_str('ASDFGHJ') == ('Too Weak!')
    assert password_str('asDF12') == ('Too Weak!')
    assert password_str('12345678') == ('Weak!')
    assert password_str('123456789876') == ('Weak!')
    assert password_str('qwertyui') == ('Weak!')
    assert password_str('qwertyuiuyt') == ('Weak!')
    assert password_str('ZXCVBNML') == ('Weak!')
    assert password_str('ASDFGHJKLI') == ('Weak!')
    assert password_str('1234asdf') == ('Good!')
    assert password_str('1234ASDF') == ('Good!')
    assert password_str('ASDFasdf') == ('Good!')
    assert password_str('1234asdfAWER') == ('Very Good!')
    assert password_str('12345678aS') == ('Very Good!')
    assert password_str('asdfghjk1A') == ('Very Good!')
    assert password_str('ASDFGTRE2a') == ('Very Good!')
