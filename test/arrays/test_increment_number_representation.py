from code.arrays.increment_number_representation import increment_number_representation


class TestBasicIncrements:
    def test_1_2_9_becomes_1_3_0(self):
        assert increment_number_representation([1, 2, 9]) == [1, 3, 0]

    def test_1_2_3_becomes_1_2_4(self):
        assert increment_number_representation([1, 2, 3]) == [1, 2, 4]

    def test_0_becomes_1(self):
        assert increment_number_representation([0]) == [1]

    def test_8_becomes_9(self):
        assert increment_number_representation([8]) == [9]


class TestCarryPropagation:
    def test_9_becomes_1_0(self):
        assert increment_number_representation([9]) == [1, 0]

    def test_9_9_9_becomes_1_0_0_0(self):
        assert increment_number_representation([9, 9, 9]) == [1, 0, 0, 0]

    def test_1_9_9_becomes_2_0_0(self):
        assert increment_number_representation([1, 9, 9]) == [2, 0, 0]

    def test_2_9_becomes_3_0(self):
        assert increment_number_representation([2, 9]) == [3, 0]


class TestEdgeCases:
    def test_single_zero(self):
        assert increment_number_representation([0]) == [1]

    def test_large_all_nines(self):
        assert increment_number_representation([9, 9, 9, 9, 9]) == [1, 0, 0, 0, 0, 0]

    def test_does_not_mutate_original_array(self):
        numbers = [1, 2, 9]
        increment_number_representation(numbers)
        assert numbers == [1, 2, 9]
