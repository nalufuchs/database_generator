CREATE TABLE profitable_products as
WITH 
prod_ord as (
SELECT * 
	FROM product 
	LEFT JOIN order_product 
	ON product.product_id = order_product.product_id), 
	
combined_table as (
SELECT (products_count * sale_value) as total_sale,
	(final_cost * products_count) as total_cost,
	* 
	FROM prod_ord 
	LEFT JOIN "order" 
	ON prod_ord.order_id = "order".order_id)

SELECT
    product_name,
    SUM((sale_value - final_cost) * products_count) AS total_profit,
    SUM(sale_value * products_count) AS total_sales,
    SUM(final_cost * products_count) AS total_cost,
    (SUM((sale_value - final_cost) * products_count) / SUM(final_cost * products_count)) * 100 AS profit_margin_percentage
FROM
    combined_table
WHERE
    sale_time >= NOW() - INTERVAL '1 year'
GROUP BY
    product_name
ORDER BY
    profit_margin_percentage DESC;