/*
https://programmers.co.kr/learn/courses/30/lessons/59413?language=oracle
Oracle로 풂.

SELECT LEVEL FROM DUAL CONNECT BY LEVEL <= 24;
1부터 24까지.
칼럼명 LEVEL을 써야 된다.

아래 문장은 정상적으로 23, 22, 21 출력.
SELECT HOUR
FROM (SELECT LEVEL-1 AS "HOUR" FROM DUAL CONNECT BY LEVEL <= 24)
ORDER BY HOUR DESC FETCH FIRST 3 ROWS ONLY;

ANIMAL_OUTS.DATETIME에서 시간만 뽑아내는 문장
select TO_CHAR(O.DATETIME,'HH24')
from ANIMAL_OUTS O;

EXTRACT(HOUR FROM ANIMAL_OUTS.DATETIME) 하면 아래 에러 발생. 왜지... extract 공부해야겠다
ORA-30076: invalid extract field for extract source

테이블 별칭을 as로 주면 아래 에러 발생
ORA-00933: SQL command not properly ended

ORA-01788: CONNECT BY clause required in this query block 에러 발생하는 아래 문장
select level from (select LEVEL-1 FROM DUAL CONNECT BY LEVEL <= 24) DUMMY;
ORA-00904: "HOUR": invalid identifier 에러 발생하는 아래 문장
select hour from (select LEVEL-1 as "hour" FROM DUAL CONNECT BY LEVEL <= 24);
위 문장에서 hour를 HOUR로 바꾸기만 해도 정상 실행됨...
select HOUR from (select LEVEL-1 as "HOUR" FROM DUAL CONNECT BY LEVEL <= 24) DUMMY;


null인 시간대의 count 값이 1로 나오는 오류가 있음.
SELECT DUMMY.HOUR, COUNT(*)
FROM (SELECT LEVEL-1 AS "HOUR" FROM DUAL CONNECT BY LEVEL <= 24) DUMMY LEFT OUTER JOIN ANIMAL_OUTS O
ON (DUMMY.HOUR = TO_CHAR(O.DATETIME,'HH24'))
GROUP BY DUMMY.HOUR
ORDER BY DUMMY.HOUR;

NVL(COUNT(*), 0)이나 DECODE(COUNT(*),NULL,0,COUNT(*))로 대체해도 마찬가지.
이러면 COUNT(*) 세기 전 부터 DUMMY 테이블에 있는 row를 하나로 셌다는 뜻.
JOIN하기 전에 미리 COUNT 해두어야 겠다.

ORA-00904: "HOUR": invalid identifier 에러 발생. HOUR를 만든 뒤 바로 GROUP BY에 쓸 수 없음.
SELECT TO_CHAR(ANIMAL_OUTS.DATETIME,'HH24') AS "HOUR", COUNT(*) AS "COUNT"
FROM ANIMAL_OUTS
GROUP BY HOUR;
아래처럼 한번 더 묶어주기
SELECT HOUR, COUNT(*) AS "COUNT"
FROM (SELECT TO_CHAR(DATETIME,'HH24') AS "HOUR", DATETIME FROM ANIMAL_OUTS)
GROUP BY HOUR;

아래 답에서 NVL(O.COUNT, 0) 말고 그냥 O.COUNT로 하면 빈칸(null) 나옴.
*/

SELECT DUMMY.HOUR, NVL(O.COUNT, 0)
FROM (SELECT LEVEL-1 AS "HOUR" FROM DUAL CONNECT BY LEVEL <= 24) DUMMY
LEFT OUTER JOIN (SELECT HOUR, COUNT(*) AS "COUNT"
FROM (SELECT TO_CHAR(DATETIME,'HH24') AS "HOUR", DATETIME FROM ANIMAL_OUTS)
GROUP BY HOUR) O
ON (DUMMY.HOUR = O.HOUR)
ORDER BY DUMMY.HOUR;