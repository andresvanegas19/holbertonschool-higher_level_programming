/*
Returns the Body Mass Index (BMI)
for all North American players from the 2017-2018 NBA season
*/


SELECT PlayerName, Country,
    ROUND(Weight_kg/SQUARE(Height_cm/100),2) BMI
FROM Players
WHERE Country = 'USA'
    OR Country = 'Canada';
-- ORDER BY BMI; Order by not required

SELECT Team,
   ROUND(AVG(BMI),2) AS AvgTeamBMI -- Alias the new column
FROM PlayerStats AS ps -- Alias PlayerStats table
INNER JOIN
		(SELECT PlayerName, Country,
			Weight_kg/SQUARE(Height_cm/100) BMI
		 FROM Players) AS p -- Alias the sub-query
             -- Alias the joining columns
	ON p.PlayerName = ps.PlayerName
GROUP BY Team
HAVING AVG(BMI) >= 25;



/*
Location of the epicenter of earthquakes with a 9+ magnitude
*/

-- Replace City with the correct column name
SELECT n.CountryName AS Country
	,e.NearestPop AS ClosestCity
    ,e.Date
    ,e.Magnitude
FROM Nations AS n
INNER JOIN Earthquakes AS e
	ON n.Code2 = e.Country
WHERE e.Magnitude >= 9
ORDER BY e.Magnitude DESC;


-- Second query

-- Add the new column to the select statement
SELECT PlayerName,
       Team,
       Position,
       AvgRebounds -- Add the new column
FROM
     -- Sub-query starts here
	(SELECT
      PlayerName,
      Team,
      Position,
      -- Calculate average total rebounds
     (ORebound+DRebound)/CAST(GamesPlayed AS numeric) AS AvgRebounds
	 FROM PlayerStats) tr
WHERE AvgRebounds >= 12; -- Filter rows

SELECT PlayerName,
      Country,
      College,
      DraftYear,
      DraftNumber
FROM Players
WHERE UPPER(LEFT(College,5)) LIKE 'LOU%'
    AND College LIKE 'Louisiana%';



SELECT Country, COUNT(*) CountOfPlayers
FROM Players
-- Add the filter condition
WHERE Country
-- Fill in the missing countries
	IN ('Argentina','Brazil','Dominican Republic'
        ,'Puerto Rico')
GROUP BY Country;


SELECT Team,
	SUM(TotalPoints) AS TotalPFPoints
FROM PlayerStats
-- Filter for only rows with power forwards
WHERE Position = 'PF'
GROUP BY Team
-- Filter for total points greater than 3000
HAVING SUM(TotalPoints) > 3000;


SELECT TOP 25 PERCENT -- Limit rows to the upper quartile
       Latitude,
       Longitude,
	   Magnitude,
	   Depth,
	   NearestPop
FROM Earthquakes
WHERE Country = 'PG'
	OR Country = 'ID'
ORDER BY Magnitude DESC; -- Order the results


SELECT NearestPop,
       Country,
       COUNT(NearestPop) NumEarthquakes -- Number of cities
FROM Earthquakes
WHERE Magnitude >= 8
	AND Country IS NOT NULL
GROUP BY NearestPop,  Country -- Group columns
ORDER BY NumEarthquakes DESC;




-- More rows are returned with UNION ALL therefore, UNION must be removing duplicates.
-- UNION ALL returns more rows than UNION because it does not remove duplicates.
-- Therefore, duplicate rows were removed with UNION.

SELECT CityName AS NearCityName,
	   CountryCode
FROM Cities
UNION ALL
SELECT Capital AS NearCityName,
       	Code2 AS CountryCode
FROM Nations;

