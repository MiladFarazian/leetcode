-- 584. Find Customer Referee
-- https://leetcode.com/problems/find-customer-referee/
-- Difficulty: Easy | Language: mysql | Runtime: 437 ms | Memory: 0.0B

# Write your MySQL query statement below
select name from customer
where referee_id != 2 or referee_id is null
