r"""TODO: port to Python.

Original JavaScript (code/misc/advance-notice-demo.js):

class AdvanceNoticeDemo {
    static MIN_TIME = { hour: 8, minute: 0 };
    static MAX_TIME = { hour: 17, minute: 0 };

    constructor(minDays, maxDays, cutOffTime, exclusions) {
        this.minDays = minDays;
        this.maxDays = maxDays;
        this.cutOffTime = cutOffTime; // { hour, minute } or null
        this.exclusions = exclusions; // AdvanceNoticeExclusionConfig or null
    }

    // --- Helper: build a full datetime object ---
    static createDateTime(year, month, day, hour = 0, minute = 0) {
        return new Date(year, month - 1, day, hour, minute);
    }

    // --- Helper: clone a date and add days ---
    static addDays(date, days) {
        const result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    }

    // --- Helper: set time on a date ---
    static atTime(date, time) {
        const result = new Date(date);
        result.setHours(time.hour, time.minute, 0, 0);
        return result;
    }

    // --- Helper: check if time is after cutOff ---
    static isAfterCutOff(date, cutOffTime) {
        const hour = date.getHours();
        const minute = date.getMinutes();
        return hour > cutOffTime.hour || (hour === cutOffTime.hour && minute > cutOffTime.minute);
    }

    // -------------------------------------------------------
    // isSaturday & isSunday
    // -------------------------------------------------------

    static isSaturday(date) {
        return date.getDay() === 6;
    }

    static isSunday(date) {
        return date.getDay() === 0;
    }

    // -------------------------------------------------------
    // isServiceDay
    // -------------------------------------------------------

    static isServiceDay(date, exclusions) {
        if (exclusions && exclusions.excludeSaturday && AdvanceNoticeDemo.isSaturday(date)) {
            return false;
        }
        if (exclusions && exclusions.excludeSunday && AdvanceNoticeDemo.isSunday(date)) {
            return false;
        }
        return true;
    }

    // -------------------------------------------------------
    // adjustRequestForward
    // -------------------------------------------------------

    adjustRequestForward(date) {
        let d = new Date(date);
        while (true) {
            if (AdvanceNoticeDemo.isSaturday(d) && this.exclusions?.excludeSaturday) {
                d = AdvanceNoticeDemo.addDays(d, 1);
                continue;
            }
            if (AdvanceNoticeDemo.isSunday(d) && this.exclusions?.excludeSunday) {
                d = AdvanceNoticeDemo.addDays(d, 1);
                continue;
            }
            return d;
        }
    }

    // -------------------------------------------------------
    // addServiceDaysExclusive
    // -------------------------------------------------------

    static addServiceDaysExclusive(start, count, exclusions) {
        if (count <= 0) return new Date(start);

        let d = new Date(start);
        let remaining = count;

        while (remaining > 0) {
            d = AdvanceNoticeDemo.addDays(d, 1);
            if (AdvanceNoticeDemo.isServiceDay(d, exclusions)) {
                remaining--;
            }
        }

        return d;
    }

    // -------------------------------------------------------
    // calculate
    // -------------------------------------------------------

    calculate(requestDateTime) {
        let baseline = new Date(requestDateTime);
        baseline.setHours(0, 0, 0, 0); // strip time — date only

        // If request is after cut-off, push baseline to next day
        if (this.cutOffTime && AdvanceNoticeDemo.isAfterCutOff(requestDateTime, this.cutOffTime)) {
            baseline = AdvanceNoticeDemo.addDays(baseline, 1);
        }

        // Adjust baseline forward past any excluded days
        baseline = this.adjustRequestForward(baseline);

        // Earliest = baseline + minDays service days
        const earliest = AdvanceNoticeDemo.addServiceDaysExclusive(baseline, this.minDays, this.exclusions);
        let minDateTime = AdvanceNoticeDemo.atTime(earliest, AdvanceNoticeDemo.MIN_TIME);

        // Latest = requestDate + maxDays at MAX_TIME
        const requestDateOnly = new Date(requestDateTime);
        requestDateOnly.setHours(0, 0, 0, 0);
        let maxDateTime = AdvanceNoticeDemo.atTime(
            AdvanceNoticeDemo.addDays(requestDateOnly, this.maxDays),
            AdvanceNoticeDemo.MAX_TIME
        );

        // Delta guard: if min has passed max, recalculate max from min
        if (minDateTime >= maxDateTime) {
            const delta = Math.max(this.maxDays - this.minDays, 0);
            maxDateTime = AdvanceNoticeDemo.atTime(
                AdvanceNoticeDemo.addDays(earliest, delta),
                AdvanceNoticeDemo.MAX_TIME
            );
        }

        return { minDateTime, maxDateTime };
    }
}

// --- Config ---
class AdvanceNoticeExclusionConfig {
    constructor(excludeSaturday, excludeSunday) {
        this.excludeSaturday = excludeSaturday;
        this.excludeSunday = excludeSunday;
    }
}

module.exports = { AdvanceNoticeDemo, AdvanceNoticeExclusionConfig };

"""
