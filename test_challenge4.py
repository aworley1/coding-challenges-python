import unittest

from challenge4 import sortVouchers


class TestChallenge4(unittest.TestCase):
    def test_correct_number_elements(self):
        """
        Should return the same number of elements as the input data
        """

        input_list = "190112:Activated:aaaa,190205:Redeemed:bbbb"

        result = sortVouchers(input_list)

        assert len(result.split(",")) == 2

        def test_return_list_if_already_sorted(self):
        """
        Should return original list if already sorted
        """

        input_list = "190112:Activated:aaaa,190205:Redeemed:bbbb"

        result = sortVouchers(input_list)

        assert len(result.split(",")) == 2


    if __name__ == '__main__':
        unittest.main()