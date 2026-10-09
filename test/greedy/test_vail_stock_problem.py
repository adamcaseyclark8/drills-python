from code.greedy.vail_stock_problem import vail_stock_problem


def test_i():
    assert vail_stock_problem([500, 750, 1000, 200, 1200, 300, 500]) == 1700
    # 250, 250, 200,


def test_ii():
    assert vail_stock_problem([500, 300, 1000, 100, 1200, 400, 500]) == 1900


def test_iii_first_element_is_highest_value():
    assert vail_stock_problem([500, 400, 300, 200, 100]) == 0


def test_iv():
    assert vail_stock_problem([500, 'two', 300, 200, 100]) == 'all values must be numeric'


def test_v():
    assert vail_stock_problem([500, -750, 1000, 200, 1200, 300, 500]) == 'all values must be positive'


def test_vi():
    assert vail_stock_problem([]) == 0


def test_vii():
    assert vail_stock_problem([500]) == 0


def test_viii():
    assert vail_stock_problem([500, 1300]) == 800
