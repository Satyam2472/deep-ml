-- your query
-- SELECT DATE_TRUNC('month', review_date) AS month, product_id, round(AVG(starts), 2) as avg_stars
-- from reviews
-- group by date_trunc('month', review_date), product_id
-- ORDER BY month, product_id;

SELECT
  date_trunc('month', review_date) AS month,
  product_id,
  ROUND(AVG(stars), 2) AS avg_stars
FROM reviews
GROUP BY date_trunc('month', review_date), product_id
ORDER BY month, product_id;