/* Write your T-SQL query statement below */
 SELECT ROUND(SUM(CASE WHEN delivery_type = 0 THEN 1 ELSE 0 END)*100.0/COUNT(*) ,2) AS immediate_percentage
 FROM 
 (SELECT *,
         DATEDIFF(day,order_date,customer_pref_delivery_date) AS delivery_type,
         RANK() OVER(PARTITION BY customer_id ORDER BY order_date) AS order_number
 FROM Delivery)t
 WHERE order_number = 1


