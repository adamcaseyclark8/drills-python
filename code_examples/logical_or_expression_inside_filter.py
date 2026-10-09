r"""TODO: port to Python.

Original JavaScript (code-examples/logical-or-expression-inside-filter.js):

// TYPESCRIPT (MY VERSION)
// const isFighterTheChampion = (history: FightHistoryEntry[], type: keyof FightHistoryEntry): boolean => {
//     if (type === 'bmf'){
//         const priorChampFights = history
//             .filter(
//                 h =>
//                     h.fight_id !== fight.id &&
//                     h[type] &&
//                     (!eventDate || new Date(h.date) < new Date(eventDate))
//             )
//             .sort((a, b) => b.date.localeCompare(a.date));
//         return priorChampFights.length > 0 && priorChampFights[0].result === 'W';
//
//     }
//
//     const priorChampFights = history
//         .filter(
//             h =>
//                 h.fight_id !== fight.id &&
//                 h[type] &&
//                 h.weightclass === fight.weightclass &&
//                 (!eventDate || new Date(h.date) < new Date(eventDate))
//         )
//         .sort((a, b) => b.date.localeCompare(a.date));
//     return priorChampFights.length > 0 && priorChampFights[0].result === 'W';

// TYPESCRIPT (REVISED)
// const isFighterTheChampion = (history: FightHistoryEntry[], type: keyof FightHistoryEntry): boolean => {
//     const priorChampFights = history
//         .filter(
//             h =>
//                 h.fight_id !== fight.id &&
//                 h[type] &&
//                 (type === 'bmf' || h.weightclass === fight.weightclass) &&
//                 (!eventDate || new Date(h.date) < new Date(eventDate))
//         )
//         .sort((a, b) => b.date.localeCompare(a.date));
//     return priorChampFights.length > 0 && priorChampFights[0].result === 'W';
// };

const isFighterTheChampion = (history, type) => {
    const priorChampFights = history
        .filter(
            h =>
                h.fight_id !== fight.id &&
                h[type] &&
                (type === 'bmf' || h.weightclass === fight.weightclass) &&
                (!eventDate || new Date(h.date) < new Date(eventDate))
        )
        .sort((a, b) => b.date.localeCompare(a.date));
    return priorChampFights.length > 0 && priorChampFights[0].result === 'W';
};

const history = [];

isFighterTheChampion(history, 'bmf');

"""
