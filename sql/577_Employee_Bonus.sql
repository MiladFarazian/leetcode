-- 577. Employee Bonus
-- https://leetcode.com/problems/employee-bonus/
-- Difficulty: Easy | Language: mysql | Runtime: 816 ms | Memory: 0.0B

SELECT Emp.name, Bonus.bonus 
FROM Employee Emp
LEFT JOIN Bonus ON Emp.empId = Bonus.empId
WHERE Bonus.bonus < 1000 or Bonus.bonus is null
