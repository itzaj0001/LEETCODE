/* Write your T-SQL query statement below */
SELECT product_id, year AS first_year, quantity, price 
FROM
(SELECT *,MIN(year) OVER (PARTITION BY product_id) as fy
FROM Sales)t
WHERE year = fy 