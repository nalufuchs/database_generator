CREATE TABLE top_100_products_sold AS
SELECT
    products.name,
    SUM(order_products.products_count) AS total_sold
FROM
    products
    INNER JOIN order_products ON products.id = order_products.product_id
    INNER JOIN orders ON order_products.order_id = orders.id
WHERE
    sale_time >= NOW() - INTERVAL '1 year'
GROUP BY
    products.name
ORDER BY
    total_sold DESC
LIMIT 100;