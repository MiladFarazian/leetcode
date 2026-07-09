-- 1757. Recyclable and Low Fat Products
-- https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Difficulty: Easy | Language: mysql | Runtime: 436 ms | Memory: 0.0B

# Write your MySQL query statement below
select product_id from products
where low_fats = "y" and recyclable = "y"
