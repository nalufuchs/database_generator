CREATE TABLE intersec_top_100_profitable_products as
SELECT
  top_100_products_sold.product_name,
  profitable_products.total_profit,
  profitable_products.total_sales,
  profitable_products.total_cost, 
  profitable_products.profit_margin_percentage
FROM
  top_100_products_sold 
  INNER JOIN profitable_products 
    ON top_100_products_sold.product_name = profitable_products.product_name 
