-- 1068. Product Sales Analysis I
-- https://leetcode.com/problems/product-sales-analysis-i/
-- Difficulty: Easy | Language: mysql | Runtime: 995 ms | Memory: 0.0B

# Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
LEFT JOIN Product ON Sales.product_id = Product.product_id
