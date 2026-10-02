SELECT a.customer_id, a.name
FROM customers a
WHERE NOT EXISTS (
    SELECT 1 
    FROM orders o 
    WHERE o.customer_id = a.customer_id
);
