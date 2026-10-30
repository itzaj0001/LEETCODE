/* Write your T-SQL query statement below */

SELECT mgr_id AS employee_id, mgr_name AS name,COUNT(reports_to) AS reports_count, ROUND(CAST(SUM(age) AS FLOAT) / COUNT(*),0) AS average_age
FROM
    (SELECT e1.employee_id AS mgr_id, e1.name AS mgr_name,e2.employee_id,e2.name,e2.reports_to,e2.age
    FROM Employees e1 
    JOIN Employees e2
    ON e1.employee_id = e2.reports_to)t
GROUP BY mgr_id,mgr_name
ORDER BY mgr_id