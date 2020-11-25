// 595e.
select name, population, area from World where area > 3000000 or population > 25000000

// 620e.
select * from cinema where MOD(id, 2) = 1 and description <> 'boring' order by rating DESC

// 627e.
update salary
    set sex = 
        case 
            when sex = 'm' then 'f' 
            when sex = 'f' then 'm'
        end

#From this problem, I learned how to write SQL query for 2 cases in single line.

// 1179e.
#Using SUM and CASE
SELECT 
id,
SUM(CASE WHEN month='Jan' THEN revenue ELSE null END) as Jan_Revenue,
SUM(CASE WHEN month='Feb' THEN revenue ELSE null END) as Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue ELSE null END) as Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue ELSE null END) as Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue ELSE null END) as May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue ELSE null END) as Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue ELSE null END) as Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue ELSE null END) as Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue ELSE null END) as Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue ELSE null END) as Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue ELSE null END) as Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue ELSE null END) as Dec_Revenue
FROM Department
GROUP BY id

#Using SUM and IF
SELECT 
id,
SUM(IF (month='Jan', revenue, null)) as Jan_Revenue,
SUM(IF (month='Feb', revenue, null)) as Feb_Revenue,
SUM(IF (month='Mar', revenue, null)) as Mar_Revenue,
SUM(IF (month='Apr', revenue, null)) as Apr_Revenue,
SUM(IF (month='May', revenue, null)) as May_Revenue,
SUM(IF (month='Jun', revenue, null)) as Jun_Revenue,
SUM(IF (month='Jul', revenue, null)) as Jul_Revenue,
SUM(IF (month='Aug', revenue, null)) as Aug_Revenue,
SUM(IF (month='Sep', revenue, null)) as Sep_Revenue,
SUM(IF (month='Oct', revenue, null)) as Oct_Revenue,
SUM(IF (month='Nov', revenue, null)) as Nov_Revenue,
SUM(IF (month='Dec', revenue, null)) as Dec_Revenue
FROM Department
GROUP BY id

#GROUP BY 절의 의미는 그룹 함수를 GROUP BY 절에 지정된 컬럼의 값이 같은 행에 대해서 통계 정보를 계산하라는 의미이다.
The meaning of the GROUP BY clause means that 
the group function calculates statistical information for rows with the same column value specified 
in the GROUP BY clause.
 
// 182e
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1
When organizing Email column using GROUP BY clause, I can use Having clause for the condition in order to searching duplication.

The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions. 
Aggregate function is a function that organize and display data like Group By.

