from roman_numerals.roman_numerals import convert


def test_convert_exists():
    assert convert


def test_one():
    num = 'I'
    actual = convert(num)
    expected = 1
    assert actual == expected


def test_two():
    num = 'II'
    actual = convert(num)
    expected = 2
    assert actual == expected


def test_four():
    num = 'IV'
    actual = convert(num)
    expected = 4
    assert actual == expected


def test_seven():
    num = 'VII'
    actual = convert(num)
    expected = 7
    assert actual == expected


def test_ten():
    num = 'X'
    actual = convert(num)
    expected = 10
    assert actual == expected


def test_40():
    num = 'XL'
    actual = convert(num)
    expected = 40
    assert actual == expected


def test_70():
    num = 'LXX'
    actual = convert(num)
    expected = 70
    assert actual == expected


def test_142():
    num = 'CXLII'
    actual = convert(num)
    expected = 142
    assert actual == expected



