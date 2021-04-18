/*
https://programmers.co.kr/learn/courses/30/lessons/59043
Oracle로 풂.

WHERE 절을 AND로 잘못 써서 ON에 이어지는 문장이 되었더니 빈 row가 줄줄 나왔음.
*/

SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_OUTS O LEFT OUTER JOIN ANIMAL_INS I
ON (O.ANIMAL_ID = I.ANIMAL_ID)
WHERE (O.DATETIME - I.DATETIME) < 0
ORDER BY I.DATETIME;