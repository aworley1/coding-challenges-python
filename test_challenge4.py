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

    def test_current_sorted(self):
        """
        Should return all Active and Available vouchers, sorted by:
        End Date Asc
        Activated
        Voucher Id
        """

        input = "190301:Activated:aaaa,190301:Available:aaaa,190301:Activated:bbbb,190301:Available:bbbb,190101:Activated:aaaa,190101:Available:aaaa,190101:Activated:bbbb,190101:Available:bbbb"

        result = sort_vouchers(input)

        assert result == "190101:Activated:aaaa,190101:Activated:bbbb,190101:Available:aaaa,190101:Available:bbbb,190301:Activated:aaaa,190301:Activated:bbbb,190301:Available:aaaa,190301:Available:bbbb"

    if __name__ == '__main__':
        unittest.main()
