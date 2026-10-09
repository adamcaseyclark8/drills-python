from code.strings.experian_split_string import experian_split_string_function


def test_string_length_is_16():
    assert experian_split_string_function('adamcaseyclarkxx', 4) == ['adam', 'case', 'ycla', 'rkxx']


def test_string_length_is_4():
    assert experian_split_string_function('adam', 4) == ['adam']


def test_string_length_is_7():
    assert experian_split_string_function('adamcas', 4) == 'string is not divisible by 4'
