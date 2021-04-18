/*
https://programmers.co.kr/learn/courses/30/lessons/59041
*/

SELECT NAME, count(*) as 'COUNT'
from ANIMAL_INS
group by NAME having count(*) > 1 and NAME is not null
order by NAME;