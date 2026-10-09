r"""TODO: port to Python.

Original JavaScript (test/misc/advance-notice-demo.test.js):

const { AdvanceNoticeDemo, AdvanceNoticeExclusionConfig } = require('../../code/misc/advance-notice-demo.js');

describe('AdvanceNoticeDemo Tests', () => {
    let weekendsExcluded;
    let noExclusions;
    let saturdayOnlyExcluded;

    const CUT_OFF = { hour: 14, minute: 0 }; // 2pm
    const sundayAsIndexOfWeek = 0;
    const mondayAsIndexOfWeek = 1;
    const tuesdayAsIndexOfWeek = 2;
    const wednesdayAsIndexOfWeek = 3;
    const thursdayAsIndexOfWeek = 4;
    const fridayAsIndexOfWeek = 5;
    const saturdayAsIndexOfWeek = 6;

    beforeEach(() => {
        weekendsExcluded = new AdvanceNoticeExclusionConfig(true, true);
        noExclusions = new AdvanceNoticeExclusionConfig(false, false);
        saturdayOnlyExcluded = new AdvanceNoticeExclusionConfig(true, false);
    });

    // -------------------------------------------------------
    // isSaturday & isSunday fn(date) [static]
    // -------------------------------------------------------

    describe('can determine saturday from date', () => {
        test('returns true for a Saturday', () => {
            const requestDayIsSaturday = new Date(2026, 2, 7); // March 7 2026 is a Saturday
            expect(AdvanceNoticeDemo.isSaturday(requestDayIsSaturday)).toBe(true);
        });

        test('returns false for a non-Saturday', () => {
            const requestDayIsMonday = new Date(2026, 2, 2); // Monday
            expect(AdvanceNoticeDemo.isSaturday(requestDayIsMonday)).toBe(false);
        });
    });

    describe('can determine sunday from date', () => {
        test('returns true for a Sunday', () => {
            const requestDayIsSunday = new Date(2026, 2, 8); // March 8 2026 is a Sunday
            expect(AdvanceNoticeDemo.isSunday(requestDayIsSunday)).toBe(true);
        });

        test('returns false for a non-Sunday', () => {
            const requestDayIsTuesday = new Date(2026, 2, 3);
            expect(AdvanceNoticeDemo.isSunday(requestDayIsTuesday)).toBe(false);
        });
    });

    // -------------------------------------------------------
    // isServiceDay fn(date, exclusions)
    // -------------------------------------------------------

    describe('can determine working days from days off', () => {
        test('Saturday is not a service day when excluded', () => {
            const requestDayIsSaturday = new Date(2026, 2, 7);
            expect(AdvanceNoticeDemo.isServiceDay(requestDayIsSaturday, weekendsExcluded)).toBe(false);
        });

        test('Sunday is not a service day when excluded', () => {
            const requestDayIsSunday = new Date(2026, 2, 8);
            expect(AdvanceNoticeDemo.isServiceDay(requestDayIsSunday, weekendsExcluded)).toBe(false);
        });

        test('Saturday IS a service day when not excluded', () => {
            const requestDayIsSaturday = new Date(2026, 2, 7);
            expect(AdvanceNoticeDemo.isServiceDay(requestDayIsSaturday, noExclusions)).toBe(true);
        });

        test('weekday is always a service day', () => {
            const monday = new Date(2026, 2, 2);
            expect(AdvanceNoticeDemo.isServiceDay(monday, weekendsExcluded)).toBe(true);
        });

        test('Saturday excluded but Sunday not: Sunday is still a service day', () => {
            const requestDayIsSunday = new Date(2026, 2, 8);
            expect(AdvanceNoticeDemo.isServiceDay(requestDayIsSunday, saturdayOnlyExcluded)).toBe(true);
        });

        test('null exclusions: all days are service days', () => {
            const requestDayIsSaturday = new Date(2026, 2, 7);
            expect(AdvanceNoticeDemo.isServiceDay(requestDayIsSaturday, null)).toBe(true);
        });
    });

    // -------------------------------------------------------
    // adjustRequestForward fn(date) => getting the day index
    // -------------------------------------------------------

    describe('adjustRequestForward', () => {
        test('weekday: no adjustment needed', () => {
            const weekendsExcludedDemo = new AdvanceNoticeDemo(3, 10, null, weekendsExcluded);
            const requestDayIsWednesday = new Date(2026, 2, 4);
            const result = weekendsExcludedDemo.adjustRequestForward(requestDayIsWednesday);
            expect(result.getDay()).toBe(wednesdayAsIndexOfWeek);
        });

        test('Saturday excluded: pushed to Monday', () => {
            const weekendsExcludedDemo = new AdvanceNoticeDemo(3, 10, null, weekendsExcluded);
            const requestDayIsSaturday = new Date(2026, 2, 7);
            const result = weekendsExcludedDemo.adjustRequestForward(requestDayIsSaturday);
            expect(result.getDay()).toBe(mondayAsIndexOfWeek);
        });

        test('Sunday excluded: pushed to Monday', () => {
            const weekendsExcludedDemo = new AdvanceNoticeDemo(3, 10, null, weekendsExcluded);
            const requestDayIsSunday = new Date(2026, 2, 8);
            const result = weekendsExcludedDemo.adjustRequestForward(requestDayIsSunday);
            expect(result.getDay()).toBe(mondayAsIndexOfWeek);
        });

        test('Saturday only excluded: Saturday pushed to Sunday, stays on Sunday', () => {
            const saturdayExcludedDemo = new AdvanceNoticeDemo(3, 10, null, saturdayOnlyExcluded);
            const requestDayIsSaturday = new Date(2026, 2, 7);
            const result = saturdayExcludedDemo.adjustRequestForward(requestDayIsSaturday);
            expect(result.getDay()).toBe(sundayAsIndexOfWeek);
        });

        test('null exclusions: Saturday stays as Saturday', () => {
            const noExclusionsDemo = new AdvanceNoticeDemo(3, 10, null, null);
            const requestDayIsSaturday = new Date(2026, 2, 7);
            const result = noExclusionsDemo.adjustRequestForward(requestDayIsSaturday);
            expect(result.getDay()).toBe(saturdayAsIndexOfWeek);
        });
    });

    // -------------------------------------------------------
    // addServiceDaysExclusive fn(request, daysOfLeadtimeNeeded, exclusions) => getting the day of the month
    // -------------------------------------------------------

    describe('addServiceDaysExclusive', () => {
        test('adds 3 service days skipping weekend', () => {
            const requestDayIsMonday = new Date(2026, 2, 2); // March 2 Monday
            const result = AdvanceNoticeDemo.addServiceDaysExclusive(requestDayIsMonday, 3, weekendsExcluded);
            expect(result.getDate()).toBe(5); // Thursday March 5
        });

        test('adds 5 service days crossing a weekend', () => {
            const requestDayIsMonday = new Date(2026, 2, 2); // March 2 Monday
            const result = AdvanceNoticeDemo.addServiceDaysExclusive(requestDayIsMonday, 5, weekendsExcluded);
            expect(result.getDate()).toBe(9); // Monday March 9
        });

        test('adds 3 calendar days when no exclusions', () => {
            const requestDayIsMonday = new Date(2026, 2, 2);
            const result = AdvanceNoticeDemo.addServiceDaysExclusive(requestDayIsMonday, 3, noExclusions);
            expect(result.getDate()).toBe(5); // Thursday March 5 (no weekend in between)
        });

        test('zero count returns start date unchanged', () => {
            const requestDayIsMonday = new Date(2026, 2, 2);
            const result = AdvanceNoticeDemo.addServiceDaysExclusive(requestDayIsMonday, 0, weekendsExcluded);
            expect(result.getDate()).toBe(2);
        });

        test('negative count returns start date unchanged', () => {
            const requestDayIsMonday = new Date(2026, 2, 2);
            const result = AdvanceNoticeDemo.addServiceDaysExclusive(requestDayIsMonday, -5, weekendsExcluded);
            expect(result.getDate()).toBe(2);
        });
    });

    // -------------------------------------------------------
    // CUT-OFF TIME LOGIC fn(request) => getting the day of the month
    // -------------------------------------------------------

    describe('calculate - cut-off time', () => {
        test('request before cut-off: baseline stays same day', () => {
            const cutOffTime2pm3DayLeadDemo = new AdvanceNoticeDemo(3, 10, CUT_OFF, noExclusions);
            const requestIsMondayAt10AM = new Date(2026, 2, 2, 10, 0); // Monday 10am
            const { minDateTime } = cutOffTime2pm3DayLeadDemo.calculate(requestIsMondayAt10AM);
            expect(minDateTime.getDate()).toBe(5); // Thursday March 5
        });

        test('request after cut-off: baseline pushed to next day', () => {
            const cutOffTime2pm3DayLeadDemo = new AdvanceNoticeDemo(3, 10, CUT_OFF, noExclusions);
            const requestIsMondayAt3PM = new Date(2026, 2, 2, 15, 0); // Monday 3pm
            const { minDateTime } = cutOffTime2pm3DayLeadDemo.calculate(requestIsMondayAt3PM);
            expect(minDateTime.getDate()).toBe(6); // Friday March 6
        });

        test('request exactly at cut-off: baseline NOT pushed (isAfter is strict)', () => {
            const cutOffTime2pm3DayLeadDemo = new AdvanceNoticeDemo(3, 10, CUT_OFF, noExclusions);
            const requestIsMondayAt2PM = new Date(2026, 2, 2, 14, 0); // Monday exactly 2pm
            const { minDateTime } = cutOffTime2pm3DayLeadDemo.calculate(requestIsMondayAt2PM);
            expect(minDateTime.getDate()).toBe(5); // Thursday March 5
        });

        test('null cut-off: baseline never pushed regardless of time', () => {
            const noCutOffTime3DayLeadDemo = new AdvanceNoticeDemo(3, 10, null, noExclusions);
            const requestIsMondayAt11PM = new Date(2026, 2, 2, 23, 0); // Monday 11pm
            const { minDateTime } = noCutOffTime3DayLeadDemo.calculate(requestIsMondayAt11PM);
            expect(minDateTime.getDate()).toBe(5); // Thursday March 5
        });
    });

    // -------------------------------------------------------
    // MIN / MAX & DELTA GUARD
    // -------------------------------------------------------

    describe('calculate - min/max and delta guard', () => {
        test('maxDateTime is requestDate + maxDays at 5pm', () => {
            const noCutOffTime3DayLeadDemo = new AdvanceNoticeDemo(3, 10, null, noExclusions);
            const requestIsMondayThe2ndAt9AM = new Date(2026, 2, 2, 9, 0); // Monday
            const { maxDateTime } = noCutOffTime3DayLeadDemo.calculate(requestIsMondayThe2ndAt9AM);
            expect(maxDateTime.getDate()).toBe(12); // March 12
            expect(maxDateTime.getHours()).toBe(17); // 5pm
        });

        test('minDateTime is always at 8am', () => {
            const noCutOffTime3DayLeadDemo = new AdvanceNoticeDemo(3, 10, null, noExclusions);
            const requestIsMondayThe2ndAt9AM = new Date(2026, 2, 2, 9, 0);
            const { minDateTime } = noCutOffTime3DayLeadDemo.calculate(requestIsMondayThe2ndAt9AM);
            expect(minDateTime.getHours()).toBe(8);
        });

        test('minDateTime is never after maxDateTime', () => {
            const cutOffTime2pm5DayLeadDemo = new AdvanceNoticeDemo(5, 7, CUT_OFF, weekendsExcluded);
            const requestIsFridayAtCutoff = new Date(2026, 1, 27, 15, 0); // Friday after cut-off
            const { minDateTime, maxDateTime } = cutOffTime2pm5DayLeadDemo.calculate(requestIsFridayAtCutoff);
            expect(minDateTime.getTime()).toBeLessThanOrEqual(maxDateTime.getTime());
        });

        test('delta guard: equal minDays and maxDays lands on same date', () => {
            const noCutOffTimeMinAndMaxEqual = new AdvanceNoticeDemo(5, 5, null, noExclusions);
            const requestIsMondayThe2ndAt9AM = new Date(2026, 2, 2, 9, 0);
            const { minDateTime, maxDateTime } = noCutOffTimeMinAndMaxEqual.calculate(requestIsMondayThe2ndAt9AM);
            expect(minDateTime.toDateString()).toBe(maxDateTime.toDateString());
        });

        test('delta guard: maxDateTime recalculated when it falls before minDateTime', () => {
            const noCutOffTimeMinAndMaxEqual = new AdvanceNoticeDemo(10, 10, null, weekendsExcluded);
            const requestIsMondayThe2ndAt9AM = new Date(2026, 2, 2, 9, 0);
            const { minDateTime, maxDateTime } = noCutOffTimeMinAndMaxEqual.calculate(requestIsMondayThe2ndAt9AM);
            expect(minDateTime.getTime()).toBeLessThanOrEqual(maxDateTime.getTime());
            expect(maxDateTime.getHours()).toBe(17); // still at 5pm
        });
    });
});

"""
