-- 1148. Article Views I
-- https://leetcode.com/problems/article-views-i/
-- Difficulty: Easy | Language: mysql | Runtime: 359 ms | Memory: 0.0B

# Write your MySQL query statement below
select distinct author_id as id from views where author_id = viewer_id
order by author_id asc
