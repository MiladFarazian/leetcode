-- 197. Rising Temperature
-- https://leetcode.com/problems/rising-temperature/
-- Difficulty: Easy | Language: mysql | Runtime: 366 ms | Memory: 0.0B

SELECT w1.id as Id 
FROM Weather w1
JOIN Weather w2 
ON DATE(w1.recordDate) = DATE(DATE_ADD(w2.recordDate, INTERVAL 1 DAY))
WHERE w1.temperature > w2.temperature
