-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- Difficulty: Easy | Language: mysql | Runtime: 1166 ms | Memory: 0.0B

SELECT EmployeeUNI.unique_id , Employees.name 
FROM Employees
LEFT JOIN EmployeeUNI 
ON Employees.id = EmployeeUNI.id;
