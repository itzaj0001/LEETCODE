/* Write your T-SQL query statement below */

SELECT ROUND(COUNT(CASE WHEN diff = 1 THEN player_id END)*1.0 / COUNT(DISTINCT player_id),2) AS fraction
FROM
(SELECT *,
        MIN(event_date) OVER(PARTITION BY player_id) AS first_date, 
        DATEDIFF(DAY,MIN(event_date) OVER(PARTITION BY player_id),event_date) AS diff
FROM activity)t