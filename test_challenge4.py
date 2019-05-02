import unittest

from challenge4 import sort_vouchers


class TestChallenge4(unittest.TestCase):
    def test_correct_number_elements(self):
        """
        Should return the same number of elements as the input data
        """

        input = "190112:Activated:aaaa,190205:Redeemed:bbbb"

        result = sort_vouchers(input)

        assert len(result.split(",")) == 2

    def test_current_come_before_old(self):
        """
        Should return all Active and Available vouchers before
        Expired and Redeemed
        """

        input = "190205:Redeemed:bbbb,190112:Expired:aaaa,190112:Activated:aaaa,190112:Available:aaaa"

        result = sort_vouchers(input)

        assert result == "190112:Activated:aaaa,190112:Available:aaaa,190205:Redeemed:bbbb,190112:Expired:aaaa"

    if __name__ == '__main__':
        unittest.main()