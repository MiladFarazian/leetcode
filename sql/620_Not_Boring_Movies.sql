-- 620. Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/
-- Difficulty: Easy | Language: mysql | Runtime: 228 ms | Memory: 0.0B

SELECT id, movie, description, rating FROM Cinema
WHERE id % 2 = 1 and description != "boring"
ORDER BY rating DESC
