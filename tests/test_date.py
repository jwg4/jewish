from datetime import date

from jewish import JewishDate

from unittest import TestCase


class TestRoundTrip(TestCase):
    def test_today(self):
        today = date.today()
        jewish = JewishDate.from_date(today)
        round_tripped = jewish.to_date()
        assert today == round_tripped
