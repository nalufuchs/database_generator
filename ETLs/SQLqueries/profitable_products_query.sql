CREATE TABLE profitable_products AS
SELECT
    products.name,
    SUM((products.sale_value - products.final_cost) * order_products.products_count) AS total_profit,
    SUM(products.sale_value * order_products.products_count) AS total_sales,
    SUM(products.final_cost * order_products.products_count) AS total_cost,
    (SUM((products.sale_value - products.final_cost) * order_products.products_count) / SUM(products.final_cost * order_products.products_count)) * 100 AS profit_margin_percentage
FROM
    products
    INNER JOIN order_products ON products.id = order_products.product_id
    INNER JOIN orders ON order_products.order_id = orders.id
WHERE
    sale_time >= NOW() - INTERVAL '1 year'
GROUP BY
    products.name
ORDER BY
    profit_margin_percentage DESC;