/*
https://programmers.co.kr/learn/courses/30/lessons/59040
*/

SELECT ANIMAL_TYPE, count(*) as 'count'
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE;