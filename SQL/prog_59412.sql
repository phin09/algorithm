/*
https://programmers.co.kr/learn/courses/30/lessons/59412
*/

SELECT hour(DATETIME) as `HOUR`, count(*) as `COUNT`
from ANIMAL_OUTS
group by `HOUR` having `HOUR` >= 9 and `HOUR` < 20
order by `HOUR`;