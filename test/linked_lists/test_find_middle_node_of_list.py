from code.linked_lists.find_middle_node_of_list import build_list, find_middle_node, list_to_array


class TestOddLengthLists:
    def test_1_2_3_middle_is_2(self):
        assert find_middle_node(build_list([1, 2, 3])).val == 2

    def test_1_2_3_4_5_middle_is_3(self):
        assert find_middle_node(build_list([1, 2, 3, 4, 5])).val == 3

    def test_10_to_70_middle_is_40(self):
        assert find_middle_node(build_list([10, 20, 30, 40, 50, 60, 70])).val == 40


class TestEvenLengthListsReturnsSecondMiddleNode:
    def test_1_2_middle_is_2(self):
        assert find_middle_node(build_list([1, 2])).val == 2

    def test_1_2_3_4_middle_is_3(self):
        assert find_middle_node(build_list([1, 2, 3, 4])).val == 3

    def test_1_2_3_4_5_6_middle_is_4(self):
        assert find_middle_node(build_list([1, 2, 3, 4, 5, 6])).val == 4


class TestTheReturnedNodeStillPointsToTheRestOfTheList:
    def test_1_2_3_4_5_middle_node_tail_is_3_4_5(self):
        assert list_to_array(find_middle_node(build_list([1, 2, 3, 4, 5]))) == [3, 4, 5]

    def test_1_2_3_4_middle_node_tail_is_3_4(self):
        assert list_to_array(find_middle_node(build_list([1, 2, 3, 4]))) == [3, 4]


class TestEdgeCases:
    def test_single_node_middle_is_1(self):
        assert find_middle_node(build_list([1])).val == 1

    def test_none_head_returns_none(self):
        assert find_middle_node(None) is None
