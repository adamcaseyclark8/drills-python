from datetime import datetime, timedelta

SATURDAY = 5  # datetime.weekday(): Monday is 0, Sunday is 6
SUNDAY = 6


class AdvanceNoticeDemo:
    MIN_TIME = {'hour': 8, 'minute': 0}
    MAX_TIME = {'hour': 17, 'minute': 0}

    def __init__(self, min_days, max_days, cut_off_time, exclusions):
        self.min_days = min_days
        self.max_days = max_days
        self.cut_off_time = cut_off_time  # {'hour', 'minute'} or None
        self.exclusions = exclusions  # AdvanceNoticeExclusionConfig or None

    # --- Helper: build a full datetime object ---
    @staticmethod
    def create_date_time(year, month, day, hour=0, minute=0):
        return datetime(year, month, day, hour, minute)

    # --- Helper: add days to a date ---
    @staticmethod
    def add_days(date, days):
        return date + timedelta(days=days)

    # --- Helper: set time on a date ---
    @staticmethod
    def at_time(date, time):
        return date.replace(hour=time['hour'], minute=time['minute'], second=0, microsecond=0)

    # --- Helper: check if time is after cut_off ---
    @staticmethod
    def is_after_cut_off(date, cut_off_time):
        hour = date.hour
        minute = date.minute
        return hour > cut_off_time['hour'] or (hour == cut_off_time['hour'] and minute > cut_off_time['minute'])

    # -------------------------------------------------------
    # is_saturday & is_sunday
    # -------------------------------------------------------

    @staticmethod
    def is_saturday(date):
        return date.weekday() == SATURDAY

    @staticmethod
    def is_sunday(date):
        return date.weekday() == SUNDAY

    # -------------------------------------------------------
    # is_service_day
    # -------------------------------------------------------

    @staticmethod
    def is_service_day(date, exclusions):
        if exclusions and exclusions.exclude_saturday and AdvanceNoticeDemo.is_saturday(date):
            return False
        if exclusions and exclusions.exclude_sunday and AdvanceNoticeDemo.is_sunday(date):
            return False
        return True

    # -------------------------------------------------------
    # adjust_request_forward
    # -------------------------------------------------------

    def adjust_request_forward(self, date):
        d = date
        while True:
            if AdvanceNoticeDemo.is_saturday(d) and self.exclusions and self.exclusions.exclude_saturday:
                d = AdvanceNoticeDemo.add_days(d, 1)
                continue
            if AdvanceNoticeDemo.is_sunday(d) and self.exclusions and self.exclusions.exclude_sunday:
                d = AdvanceNoticeDemo.add_days(d, 1)
                continue
            return d

    # -------------------------------------------------------
    # add_service_days_exclusive
    # -------------------------------------------------------

    @staticmethod
    def add_service_days_exclusive(start, count, exclusions):
        if count <= 0:
            return start

        d = start
        remaining = count

        while remaining > 0:
            d = AdvanceNoticeDemo.add_days(d, 1)
            if AdvanceNoticeDemo.is_service_day(d, exclusions):
                remaining -= 1

        return d

    # -------------------------------------------------------
    # calculate
    # -------------------------------------------------------

    def calculate(self, request_date_time):
        baseline = request_date_time.replace(hour=0, minute=0, second=0, microsecond=0)  # strip time — date only

        # If request is after cut-off, push baseline to next day
        if self.cut_off_time and AdvanceNoticeDemo.is_after_cut_off(request_date_time, self.cut_off_time):
            baseline = AdvanceNoticeDemo.add_days(baseline, 1)

        # Adjust baseline forward past any excluded days
        baseline = self.adjust_request_forward(baseline)

        # Earliest = baseline + min_days service days
        earliest = AdvanceNoticeDemo.add_service_days_exclusive(baseline, self.min_days, self.exclusions)
        min_date_time = AdvanceNoticeDemo.at_time(earliest, AdvanceNoticeDemo.MIN_TIME)

        # Latest = request_date + max_days at MAX_TIME
        request_date_only = request_date_time.replace(hour=0, minute=0, second=0, microsecond=0)
        max_date_time = AdvanceNoticeDemo.at_time(
            AdvanceNoticeDemo.add_days(request_date_only, self.max_days),
            AdvanceNoticeDemo.MAX_TIME,
        )

        # Delta guard: if min has passed max, recalculate max from min
        if min_date_time >= max_date_time:
            delta = max(self.max_days - self.min_days, 0)
            max_date_time = AdvanceNoticeDemo.at_time(
                AdvanceNoticeDemo.add_days(earliest, delta),
                AdvanceNoticeDemo.MAX_TIME,
            )

        return {'min_date_time': min_date_time, 'max_date_time': max_date_time}


# --- Config ---
class AdvanceNoticeExclusionConfig:
    def __init__(self, exclude_saturday, exclude_sunday):
        self.exclude_saturday = exclude_saturday
        self.exclude_sunday = exclude_sunday
