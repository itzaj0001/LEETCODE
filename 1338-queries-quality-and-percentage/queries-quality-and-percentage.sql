/* Write your T-SQL query statement below */
SELECT query_name,  
       ROUND(AVG(CAST(rating as FLOAT) / position),2) AS quality,
       ROUND(AVG(CASE WHEN rating >= 3 THEN 0.0 ELSE 100.0 END),2) AS poor_query_percentage
 FROM Queries
GROUP BY query_name