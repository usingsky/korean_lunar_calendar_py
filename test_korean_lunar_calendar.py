# -*- coding: utf-8 -*-
"""
Tests for KoreanLunarCalendar.

Run from this directory:
    python -m unittest -v

Expected values are taken from the KARI standard (cross-checked against the
JavaScript/Java ports of this library).
"""
import datetime
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from korean_lunar_calendar import KoreanLunarCalendar


class SolarToLunarTest(unittest.TestCase):
    def test_known_conversions(self):
        cal = KoreanLunarCalendar()

        self.assertTrue(cal.setSolarDate(2017, 6, 24))
        self.assertEqual(cal.LunarIsoFormat(), "2017-05-01 Intercalation")
        self.assertEqual(cal.getGapJaString(), "정유년 병오월 임오일 (윤월)")
        self.assertEqual(cal.getChineseGapJaString(), "丁酉年 丙午月 壬午日 (閏月)")

        self.assertTrue(cal.setSolarDate(1956, 3, 3))
        self.assertEqual(cal.LunarIsoFormat(), "1956-01-21")
        self.assertEqual(cal.getGapJaString(), "병신년 경인월 기사일")
        self.assertEqual(cal.getChineseGapJaString(), "丙申年 庚寅月 己巳日")

        self.assertTrue(cal.setSolarDate(1000, 2, 13))  # minimum supported solar date
        self.assertEqual(cal.LunarIsoFormat(), "1000-01-01")
        self.assertEqual(cal.getGapJaString(), "경자년 무인월 기묘일")

        self.assertTrue(cal.setSolarDate(2050, 12, 31))  # maximum supported solar date
        self.assertEqual(cal.LunarIsoFormat(), "2050-11-18")
        self.assertEqual(cal.getGapJaString(), "경오년 무자월 을유일")

        self.assertTrue(cal.setSolarDate(1727, 4, 21))  # falls on a leap-month lunar date
        self.assertEqual(cal.LunarIsoFormat(), "1727-03-01 Intercalation")
        self.assertEqual(cal.getGapJaString(), "정미년 갑진월 정사일 (윤월)")
        self.assertEqual(cal.getChineseGapJaString(), "丁未年 甲辰月 丁巳日 (閏月)")


class LunarToSolarTest(unittest.TestCase):
    def test_known_conversions(self):
        cal = KoreanLunarCalendar()

        self.assertTrue(cal.setLunarDate(2017, 5, 1, True))  # intercalation (leap) month
        self.assertEqual(cal.SolarIsoFormat(), "2017-06-24")

        self.assertTrue(cal.setLunarDate(1956, 1, 21, False))
        self.assertEqual(cal.SolarIsoFormat(), "1956-03-03")

        self.assertTrue(cal.setLunarDate(1320, 11, 24, False))
        self.assertEqual(cal.SolarIsoFormat(), "1321-01-01")

        # Leap (intercalation) month: lunar 1727-03-01 (leap) -> solar 1727-04-21
        self.assertTrue(cal.setLunarDate(1727, 3, 1, True))
        self.assertEqual(cal.SolarIsoFormat(), "1727-04-21")
        self.assertEqual(cal.getGapJaString(), "정미년 갑진월 정사일 (윤월)")


class DefaultDateTest(unittest.TestCase):
    def test_defaults_to_today(self):
        cal = KoreanLunarCalendar()
        today = datetime.date.today()
        self.assertEqual(cal.solarYear, today.year)
        self.assertEqual(cal.solarMonth, today.month)
        self.assertEqual(cal.solarDay, today.day)


class ValidationTest(unittest.TestCase):
    def test_invalid_dates_rejected(self):
        cal = KoreanLunarCalendar()

        # Out of supported range.
        self.assertFalse(cal.setLunarDate(999, 1, 1, False))
        self.assertFalse(cal.setSolarDate(2051, 1, 1))

        # 1582.10.5 ~ 1582.10.14 were removed by the Gregorian reform.
        self.assertFalse(cal.setSolarDate(1582, 10, 8))
        # October 1582 still ends at day 31; days beyond that must be rejected.
        self.assertFalse(cal.setSolarDate(1582, 10, 35))

        # A leap month can only be requested when the year actually has one in
        # that position; month 3 of 2017 is not a leap month.
        self.assertFalse(cal.setLunarDate(2017, 3, 1, True))

        # Non-integer inputs are rejected instead of corrupting the math.
        self.assertFalse(cal.setSolarDate(2017, 6, 24.5))

    def test_valid_boundary_dates_accepted(self):
        cal = KoreanLunarCalendar()

        self.assertTrue(cal.setLunarDate(1000, 1, 1, False))
        self.assertTrue(cal.setSolarDate(2050, 12, 31))
        self.assertTrue(cal.setSolarDate(1582, 10, 4))   # day just before the gap
        self.assertTrue(cal.setSolarDate(1582, 10, 15))  # day just after the gap
        self.assertTrue(cal.setLunarDate(2017, 5, 1, True))  # real leap month


if __name__ == "__main__":
    unittest.main()
