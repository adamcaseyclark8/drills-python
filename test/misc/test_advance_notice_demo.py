import calendar
from datetime import datetime

import pytest

from code.misc.advance_notice_demo import AdvanceNoticeDemo, AdvanceNoticeExclusionConfig

CUT_OFF = {'hour': 14, 'minute': 0}  # 2pm


@pytest.fixture
def weekends_excluded():
    return AdvanceNoticeExclusionConfig(True, True)


@pytest.fixture
def no_exclusions():
    return AdvanceNoticeExclusionConfig(False, False)


@pytest.fixture
def saturday_only_excluded():
    return AdvanceNoticeExclusionConfig(True, False)


# -------------------------------------------------------
# is_saturday & is_sunday fn(date) [static]
# -------------------------------------------------------


class TestCanDetermineSaturdayFromDate:
    def test_returns_true_for_a_saturday(self):
        request_day_is_saturday = datetime(2026, 3, 7)  # March 7 2026 is a Saturday
        assert AdvanceNoticeDemo.is_saturday(request_day_is_saturday) is True

    def test_returns_false_for_a_non_saturday(self):
        request_day_is_monday = datetime(2026, 3, 2)  # Monday
        assert AdvanceNoticeDemo.is_saturday(request_day_is_monday) is False


class TestCanDetermineSundayFromDate:
    def test_returns_true_for_a_sunday(self):
        request_day_is_sunday = datetime(2026, 3, 8)  # March 8 2026 is a Sunday
        assert AdvanceNoticeDemo.is_sunday(request_day_is_sunday) is True

    def test_returns_false_for_a_non_sunday(self):
        request_day_is_tuesday = datetime(2026, 3, 3)
        assert AdvanceNoticeDemo.is_sunday(request_day_is_tuesday) is False


# -------------------------------------------------------
# is_service_day fn(date, exclusions)
# -------------------------------------------------------


class TestCanDetermineWorkingDaysFromDaysOff:
    def test_saturday_is_not_a_service_day_when_excluded(self, weekends_excluded):
        assert AdvanceNoticeDemo.is_service_day(datetime(2026, 3, 7), weekends_excluded) is False

    def test_sunday_is_not_a_service_day_when_excluded(self, weekends_excluded):
        assert AdvanceNoticeDemo.is_service_day(datetime(2026, 3, 8), weekends_excluded) is False

    def test_saturday_is_a_service_day_when_not_excluded(self, no_exclusions):
        assert AdvanceNoticeDemo.is_service_day(datetime(2026, 3, 7), no_exclusions) is True

    def test_weekday_is_always_a_service_day(self, weekends_excluded):
        monday = datetime(2026, 3, 2)
        assert AdvanceNoticeDemo.is_service_day(monday, weekends_excluded) is True

    def test_saturday_excluded_but_sunday_not_sunday_is_still_a_service_day(self, saturday_only_excluded):
        assert AdvanceNoticeDemo.is_service_day(datetime(2026, 3, 8), saturday_only_excluded) is True

    def test_none_exclusions_all_days_are_service_days(self):
        assert AdvanceNoticeDemo.is_service_day(datetime(2026, 3, 7), None) is True


# -------------------------------------------------------
# adjust_request_forward fn(date) => getting the day index
# -------------------------------------------------------


class TestAdjustRequestForward:
    def test_weekday_no_adjustment_needed(self, weekends_excluded):
        demo = AdvanceNoticeDemo(3, 10, None, weekends_excluded)
        result = demo.adjust_request_forward(datetime(2026, 3, 4))
        assert result.weekday() == calendar.WEDNESDAY

    def test_saturday_excluded_pushed_to_monday(self, weekends_excluded):
        demo = AdvanceNoticeDemo(3, 10, None, weekends_excluded)
        result = demo.adjust_request_forward(datetime(2026, 3, 7))
        assert result.weekday() == calendar.MONDAY

    def test_sunday_excluded_pushed_to_monday(self, weekends_excluded):
        demo = AdvanceNoticeDemo(3, 10, None, weekends_excluded)
        result = demo.adjust_request_forward(datetime(2026, 3, 8))
        assert result.weekday() == calendar.MONDAY

    def test_saturday_only_excluded_saturday_pushed_to_sunday_stays_on_sunday(self, saturday_only_excluded):
        demo = AdvanceNoticeDemo(3, 10, None, saturday_only_excluded)
        result = demo.adjust_request_forward(datetime(2026, 3, 7))
        assert result.weekday() == calendar.SUNDAY

    def test_none_exclusions_saturday_stays_as_saturday(self):
        demo = AdvanceNoticeDemo(3, 10, None, None)
        result = demo.adjust_request_forward(datetime(2026, 3, 7))
        assert result.weekday() == calendar.SATURDAY


# -------------------------------------------------------
# add_service_days_exclusive fn(request, days_of_leadtime_needed, exclusions) => getting the day of the month
# -------------------------------------------------------


class TestAddServiceDaysExclusive:
    def test_adds_3_service_days_skipping_weekend(self, weekends_excluded):
        request_day_is_monday = datetime(2026, 3, 2)  # March 2 Monday
        result = AdvanceNoticeDemo.add_service_days_exclusive(request_day_is_monday, 3, weekends_excluded)
        assert result.day == 5  # Thursday March 5

    def test_adds_5_service_days_crossing_a_weekend(self, weekends_excluded):
        request_day_is_monday = datetime(2026, 3, 2)  # March 2 Monday
        result = AdvanceNoticeDemo.add_service_days_exclusive(request_day_is_monday, 5, weekends_excluded)
        assert result.day == 9  # Monday March 9

    def test_adds_3_calendar_days_when_no_exclusions(self, no_exclusions):
        result = AdvanceNoticeDemo.add_service_days_exclusive(datetime(2026, 3, 2), 3, no_exclusions)
        assert result.day == 5  # Thursday March 5 (no weekend in between)

    def test_zero_count_returns_start_date_unchanged(self, weekends_excluded):
        result = AdvanceNoticeDemo.add_service_days_exclusive(datetime(2026, 3, 2), 0, weekends_excluded)
        assert result.day == 2

    def test_negative_count_returns_start_date_unchanged(self, weekends_excluded):
        result = AdvanceNoticeDemo.add_service_days_exclusive(datetime(2026, 3, 2), -5, weekends_excluded)
        assert result.day == 2


# -------------------------------------------------------
# CUT-OFF TIME LOGIC fn(request) => getting the day of the month
# -------------------------------------------------------


class TestCalculateCutOffTime:
    def test_request_before_cut_off_baseline_stays_same_day(self, no_exclusions):
        demo = AdvanceNoticeDemo(3, 10, CUT_OFF, no_exclusions)
        request_is_monday_at_10am = datetime(2026, 3, 2, 10, 0)  # Monday 10am
        assert demo.calculate(request_is_monday_at_10am)['min_date_time'].day == 5  # Thursday March 5

    def test_request_after_cut_off_baseline_pushed_to_next_day(self, no_exclusions):
        demo = AdvanceNoticeDemo(3, 10, CUT_OFF, no_exclusions)
        request_is_monday_at_3pm = datetime(2026, 3, 2, 15, 0)  # Monday 3pm
        assert demo.calculate(request_is_monday_at_3pm)['min_date_time'].day == 6  # Friday March 6

    def test_request_exactly_at_cut_off_baseline_not_pushed_is_after_is_strict(self, no_exclusions):
        demo = AdvanceNoticeDemo(3, 10, CUT_OFF, no_exclusions)
        request_is_monday_at_2pm = datetime(2026, 3, 2, 14, 0)  # Monday exactly 2pm
        assert demo.calculate(request_is_monday_at_2pm)['min_date_time'].day == 5  # Thursday March 5

    def test_none_cut_off_baseline_never_pushed_regardless_of_time(self, no_exclusions):
        demo = AdvanceNoticeDemo(3, 10, None, no_exclusions)
        request_is_monday_at_11pm = datetime(2026, 3, 2, 23, 0)  # Monday 11pm
        assert demo.calculate(request_is_monday_at_11pm)['min_date_time'].day == 5  # Thursday March 5


# -------------------------------------------------------
# MIN / MAX & DELTA GUARD
# -------------------------------------------------------


class TestCalculateMinMaxAndDeltaGuard:
    def test_max_date_time_is_request_date_plus_max_days_at_5pm(self, no_exclusions):
        demo = AdvanceNoticeDemo(3, 10, None, no_exclusions)
        max_date_time = demo.calculate(datetime(2026, 3, 2, 9, 0))['max_date_time']  # Monday
        assert max_date_time.day == 12  # March 12
        assert max_date_time.hour == 17  # 5pm

    def test_min_date_time_is_always_at_8am(self, no_exclusions):
        demo = AdvanceNoticeDemo(3, 10, None, no_exclusions)
        assert demo.calculate(datetime(2026, 3, 2, 9, 0))['min_date_time'].hour == 8

    def test_min_date_time_is_never_after_max_date_time(self, weekends_excluded):
        demo = AdvanceNoticeDemo(5, 7, CUT_OFF, weekends_excluded)
        request_is_friday_after_cutoff = datetime(2026, 2, 27, 15, 0)  # Friday after cut-off
        result = demo.calculate(request_is_friday_after_cutoff)
        assert result['min_date_time'] <= result['max_date_time']

    def test_delta_guard_equal_min_days_and_max_days_lands_on_same_date(self, no_exclusions):
        demo = AdvanceNoticeDemo(5, 5, None, no_exclusions)
        result = demo.calculate(datetime(2026, 3, 2, 9, 0))
        assert result['min_date_time'].date() == result['max_date_time'].date()

    def test_delta_guard_max_date_time_recalculated_when_it_falls_before_min_date_time(self, weekends_excluded):
        demo = AdvanceNoticeDemo(10, 10, None, weekends_excluded)
        result = demo.calculate(datetime(2026, 3, 2, 9, 0))
        assert result['min_date_time'] <= result['max_date_time']
        assert result['max_date_time'].hour == 17  # still at 5pm
