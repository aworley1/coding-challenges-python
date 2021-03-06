import unittest

from challenge4.sort_vouchers import sortVouchers

class TestChallenge4(unittest.TestCase):
    def test_correct_number_elements(self):
        """
        Should return the same number of elements as the input data
        """

        input = "190112:Activated:aaaa,190205:Redeemed:bbbb"

        result = sortVouchers(input)

        assert len(result.split(",")) == 2

    def test_current_come_before_old(self):
        """
        Should return all Active and Available vouchers before
        Expired and Redeemed
        """

        input = "190205:Redeemed:bbbb,190112:Expired:aaaa,190112:Activated:aaaa,190112:Available:aaaa"

        result = sortVouchers(input)

        assert result == "190112:Activated:aaaa,190112:Available:aaaa,190205:Redeemed:bbbb,190112:Expired:aaaa"

    def test_current_sorted(self):
        """
        Should return all Active and Available vouchers, sorted by:
        End Date Asc
        Activated
        Voucher Id
        """

        input = "190301:Activated:aaaa,190301:Available:aaaa,190301:Activated:bbbb,190301:Available:bbbb,190101:Activated:aaaa,190101:Available:aaaa,190101:Activated:bbbb,190101:Available:bbbb"

        result = sortVouchers(input)

        assert result == "190101:Activated:aaaa,190101:Activated:bbbb,190101:Available:aaaa,190101:Available:bbbb,190301:Activated:aaaa,190301:Activated:bbbb,190301:Available:aaaa,190301:Available:bbbb"


    def test_old_sorted(self):
        """
        Should return all Redeemed and Expired vouchers, sorted by:
        End Date Desc
        Redeemed, then expired
        Voucher Id Asc
        """

        input = "190101:Expired:aaaa,190101:Redeemed:aaaa,190101:Expired:bbbb,190101:Redeemed:bbbb,190301:Expired:aaaa,190301:Redeemed:aaaa,190301:Expired:bbbb,190301:Redeemed:bbbb"

        result = sortVouchers(input)

        assert result == "190301:Redeemed:aaaa,190301:Redeemed:bbbb,190301:Expired:aaaa,190301:Expired:bbbb,190101:Redeemed:aaaa,190101:Redeemed:bbbb,190101:Expired:aaaa,190101:Expired:bbbb"

    def test_sort_the_example(self):
        """
        Should sort the example properly
        """

        input = "190112:Available:aaaa,190112:Activated:bbbb,190111:Available:cccc,190110:Redeemed:dddd,190110:Expired:eeee,190111:Activated:ffff"

        result = sortVouchers(input)

        assert result == "190111:Activated:ffff,190111:Available:cccc,190112:Activated:bbbb,190112:Available:aaaa,190110:Redeemed:dddd,190110:Expired:eeee"

    if __name__ == '__main__':
        unittest.main()
