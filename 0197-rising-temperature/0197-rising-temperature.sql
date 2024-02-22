# Write your MySQL query statement below
 
SELECT c.id
FROM Weather c
WHERE c.temperature > (
    SELECT p.temperature
    FROM Weather p
    WHERE p.recordDate = DATE_SUB(c.recordDate, INTERVAL 1 DAY)
)
