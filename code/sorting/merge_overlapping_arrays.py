def merge_overlapping_arrays(intervals):
    if len(intervals) == 0:
        return []

    # A flat list isn't a list of intervals, so there is nothing to merge
    if not isinstance(intervals[0], list):
        return intervals

    # Sort intervals by their start times
    intervals.sort(key=lambda interval: interval[0])

    # Start with the first interval
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # Check if current overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge by updating the end of the last merged interval if needed
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, just add the current interval
            merged.append(current)

    return merged
