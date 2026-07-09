-- 1661. Average Time of Process per Machine
-- https://leetcode.com/problems/average-time-of-process-per-machine/
-- Difficulty: Easy | Language: mysql | Runtime: 983 ms | Memory: 0.0B

WITH ProcessRuntimes AS (
    SELECT 
        machine_id,
        process_id,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) - 
        MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS runtime
    FROM 
        Activity
    GROUP BY 
        machine_id, 
        process_id
)

SELECT 
    machine_id,
    ROUND(AVG(runtime),3) AS processing_time
FROM 
    ProcessRuntimes
GROUP BY 
    machine_id;
