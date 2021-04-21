/*
https://programmers.co.kr/learn/courses/30/lessons/59044
Oracle로 풂.
*/

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT OUTER JOIN ANIMAL_OUTS O
ON (I.ANIMAL_ID = O.ANIMAL_ID)
WHERE O.DATETIME is null
ORDER BY I.DATETIME FETCH FIRST 3 ROWS ONLY;