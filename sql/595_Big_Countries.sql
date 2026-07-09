-- 595. Big Countries
-- https://leetcode.com/problems/big-countries/
-- Difficulty: Easy | Language: mysql | Runtime: 258 ms | Memory: 0.0B

# Write your MySQL query statement below
select name, population, area from world
where area >= 3000000 or population >= 25000000
