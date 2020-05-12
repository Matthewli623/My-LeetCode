# Write your
MySQL query statement below
select Name as Employee
from Employee e
where e.Salary>(select salary
from Employee e2
where e.ManagerId=e2.Id);