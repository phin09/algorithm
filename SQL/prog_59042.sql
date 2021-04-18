/*
https://programmers.co.kr/learn/courses/30/lessons/59042
Oracle로 풂.

JOIN 방향에 대한 개념정리 필요
*/

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O LEFT OUTER JOIN ANIMAL_INS I
ON (I.ANIMAL_ID = O.ANIMAL_ID)
WHERE I.ANIMAL_ID is null
ORDER BY ANIMAL_ID;