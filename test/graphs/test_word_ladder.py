from code.graphs.word_ladder import word_ladder_length


def test_returns_correct_steps_for_a_typical_transformation():
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    assert word_ladder_length('hit', 'cog', word_list) == 5
    # hit → hot → dot → dog → cog


def test_returns_0_if_end_is_not_in_list():
    word_list = ['hot', 'dot', 'dog', 'lot', 'log']  # no 'cog'
    assert word_ladder_length('hit', 'cog', word_list) == 0


def test_returns_0_if_no_path_exists():
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'xyz']  # 'cog' disconnected
    assert word_ladder_length('hit', 'cog', word_list) == 0


def test_handles_single_letter_words():
    assert word_ladder_length('a', 'c', ['a', 'b', 'c']) == 2
    # a → c


def test_begin_equals_end():
    assert word_ladder_length('same', 'same', ['same', 'came', 'lame']) == 1


def test_large_transformation_path():
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog', 'hog', 'cot']
    # multiple paths exist, shortest path length = 4
    assert word_ladder_length('hit', 'cog', word_list) == 4
    # hit → hot → hog → cog


def test_empty_word_list():
    assert word_ladder_length('hit', 'cog', []) == 0
