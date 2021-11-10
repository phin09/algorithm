/*
https://leetcode.com/problems/duplicate-emails/

not equal to operator
1. <> 는 rows 반환
2. != 0 또는 1 반환

self join하면 on 조건에 맞는 모든 조합을 만듦

union의 결과는 distinct한 것과 같음

-- 안되는 것 - 왜 안되는지 알고 싶음
-- Every derived table must have its own alias
select p1.email
from Person p1
join (select distinct(email) from Person p2)
on p1.email = p2.email
where p1.email <> p2.email;
 */

-- 방법 1
-- group by + having
select email
from Person
group by email
having count(*) > 1;


-- 방법 2
-- self join, <>
select distinct(p1.email) from Person p1
join Person p2
on p1.email = p2.email
where p1.id <> p2.id;