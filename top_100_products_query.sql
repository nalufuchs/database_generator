CREATE TABLE top_100_products_sold as
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
    SUM(products_count) AS total_sold
FROM
    combined_table
WHERE
    sale_time >= NOW() - INTERVAL '1 year'
GROUP BY
    product_name
ORDER BY
    total_sold DESC
LIMIT 100;