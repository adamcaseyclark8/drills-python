from code.recursion.deep_clone_object import deep_clone_object


def test_basic_shallow_object():
    obj = {'a': 1, 'b': 2}
    clone = deep_clone_object(obj)
    assert clone == obj
    assert clone is not obj


def test_nested_object_is_a_new_reference():
    obj = {'a': 1, 'b': {'c': 2}}
    clone = deep_clone_object(obj)
    assert clone == obj
    assert clone['b'] is not obj['b']


def test_nested_arrays():
    obj = {'a': [1, 2, 3]}
    clone = deep_clone_object(obj)
    assert clone == obj
    assert clone['a'] is not obj['a']


def test_deeply_nested_object():
    obj = {'a': {'b': {'c': {'d': 4}}}}
    clone = deep_clone_object(obj)
    assert clone == obj
    assert clone['a']['b']['c'] is not obj['a']['b']['c']


def test_none_value():
    assert deep_clone_object(None) is None


def test_primitive_value():
    assert deep_clone_object(42) == 42


def test_array_of_objects():
    obj = [{'a': 1}, {'b': 2}]
    clone = deep_clone_object(obj)
    assert clone == obj
    assert clone[0] is not obj[0]
