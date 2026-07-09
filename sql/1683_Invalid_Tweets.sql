-- 1683. Invalid Tweets
-- https://leetcode.com/problems/invalid-tweets/
-- Difficulty: Easy | Language: mysql | Runtime: 622 ms | Memory: 0.0B

# Write your MySQL query statement below
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15
