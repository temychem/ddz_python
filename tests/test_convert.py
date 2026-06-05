from excel.convert import (
    extract_max_score,
    clean_score,
    convert_to_scale
)


def test_extract_max_score():
    assert extract_max_score("Тест 10 вопрос") == 10
    assert extract_max_score("Экзамен 25 вопросов") == 25
    assert extract_max_score("Без числа") is None


def test_clean_score():
    assert clean_score("10") == 10.0
    assert clean_score(5) == 5.0
    assert clean_score("-") is None
    assert clean_score(None) is None
    assert clean_score("abc") is None


def test_convert_to_scale_5():
    result = convert_to_scale(
        score=9,
        max_score=10
    )

    assert result == 5


def test_convert_to_scale_4():
    result = convert_to_scale(
        score=7,
        max_score=10
    )

    assert result == 4


def test_convert_to_scale_3():
    result = convert_to_scale(
        score=5,
        max_score=10
    )

    assert result == 3


def test_convert_to_scale_2():
    result = convert_to_scale(
        score=3,
        max_score=10
    )

    assert result == 2


def test_convert_to_scale_1():
    result = convert_to_scale(
        score=1,
        max_score=10
    )

    assert result == 1


def test_convert_to_scale_0():
    result = convert_to_scale(
        score=0,
        max_score=10
    )

    assert result == 0


def test_convert_to_scale_none():
    result = convert_to_scale(
        score=None,
        max_score=10
    )

    assert result is None