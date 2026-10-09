# TYPESCRIPT (MY VERSION)
# const isFighterTheChampion = (history: FightHistoryEntry[], type: keyof FightHistoryEntry): boolean => {
#     if (type === 'bmf'){
#         const priorChampFights = history
#             .filter(
#                 h =>
#                     h.fight_id !== fight.id &&
#                     h[type] &&
#                     (!eventDate || new Date(h.date) < new Date(eventDate))
#             )
#             .sort((a, b) => b.date.localeCompare(a.date));
#         return priorChampFights.length > 0 && priorChampFights[0].result === 'W';
#
#     }
#
#     const priorChampFights = history
#         .filter(
#             h =>
#                 h.fight_id !== fight.id &&
#                 h[type] &&
#                 h.weightclass === fight.weightclass &&
#                 (!eventDate || new Date(h.date) < new Date(eventDate))
#         )
#         .sort((a, b) => b.date.localeCompare(a.date));
#     return priorChampFights.length > 0 && priorChampFights[0].result === 'W';

# TYPESCRIPT (REVISED)
# const isFighterTheChampion = (history: FightHistoryEntry[], type: keyof FightHistoryEntry): boolean => {
#     const priorChampFights = history
#         .filter(
#             h =>
#                 h.fight_id !== fight.id &&
#                 h[type] &&
#                 (type === 'bmf' || h.weightclass === fight.weightclass) &&
#                 (!eventDate || new Date(h.date) < new Date(eventDate))
#         )
#         .sort((a, b) => b.date.localeCompare(a.date));
#     return priorChampFights.length > 0 && priorChampFights[0].result === 'W';
# };

# PYTHON
# `fight` and `event_date` come from the surrounding scope in the original;
# they're parameters here so the example runs on its own. Dates are ISO strings,
# so comparing them as strings orders them correctly.


def is_fighter_the_champion(history, type, fight, event_date=None):
    prior_champ_fights = sorted(
        (
            h
            for h in history
            if h['fight_id'] != fight['id']
            and h.get(type)
            and (type == 'bmf' or h['weightclass'] == fight['weightclass'])
            and (not event_date or h['date'] < event_date)
        ),
        key=lambda h: h['date'],
        reverse=True,
    )
    return len(prior_champ_fights) > 0 and prior_champ_fights[0]['result'] == 'W'


if __name__ == '__main__':
    history = []

    print(is_fighter_the_champion(history, 'bmf', {'id': 1, 'weightclass': 'welterweight'}))
