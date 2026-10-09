SELECT country, COUNT(*) as athlete_count
FROM olympic
GROUP BY country
HAVING COUNT(*) > 5

SELECT country, COUNT(DISTINCT athleteName) as athlete_count
FROM olympic
GROUP BY country
HAVING COUNT(DISTINCT athleteName) > 5