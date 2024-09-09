CREATE TABLE intersec_top_100_profitable_products as
<<<<<<< HEAD
SELECT top_100_products_sold.product_name, profitable_products.total_profit, profitable_products.total_sales, profitable_products.total_cost, profitable_products.profit_margin_percentage FROM top_100_products_sold INNER JOIN profitable_products ON top_100_products_sold.product_name = profitable_products.product_name 
=======
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
>>>>>>> 6f6989d158574c91d3af221a6f589f97a82d6711
