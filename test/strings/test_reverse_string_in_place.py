from code.strings.reverse_string_in_place import reverse_string_in_place


def test_standard_example():
    assert reverse_string_in_place('not of this world') == 'dlrow siht fo ton'


def test_another_standard_example():
    assert reverse_string_in_place('hello') == 'olleh'


def test_yet_another_standard_example():
    assert reverse_string_in_place('Howdy') == 'ydwoH'


def test_string_with_spaces():
    assert reverse_string_in_place('Greetings from Earth') == 'htraE morf sgniteerG'


def test_string_with_one_character():
    assert reverse_string_in_place('b') == 'b'
