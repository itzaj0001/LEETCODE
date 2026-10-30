/* Write your T-SQL query statement below */
SELECT sell_date, COUNT(*) AS num_sold, STRING_AGG(product , ',') AS products
FROM(
SELECT DISTINCT *
FROM Activities)t
GROUP BY sell_date