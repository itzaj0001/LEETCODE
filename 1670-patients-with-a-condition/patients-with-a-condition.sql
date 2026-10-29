/* Write your T-SQL query statement below */

SELECT *
FROM Patients p
WHERE EXISTS (
    SELECT 1
    FROM STRING_SPLIT(p.conditions, ' ') s
    WHERE s.value LIKE 'DIAB1%'
);

