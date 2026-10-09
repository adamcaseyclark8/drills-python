def perform_activity_selection(activities):
    ordered = sorted(activities, key=lambda activity: activity['end'])
    selected = [ordered[0]]
    last_end = ordered[0]['end']

    for i in range(1, len(ordered)):
        if ordered[i]['start'] >= last_end:
            selected.append(ordered[i])
            last_end = ordered[i]['end']

    return selected
