/*
https://programmers.co.kr/learn/courses/30/lessons/59409
Oracle로 풂.

REGEXP_LIKE 참고 링크
https://jhnyang.tistory.com/292

ORA-00923: FROM keyword not found where expected 오류 난 문장. 이게 왜???
-> alias를 ""가 아니고 ''로 줘서.......
SELECT ANIMAL_ID, NAME, CASE WHEN SEX_UPON_INTAKE LIKE 'Intact%' THEN 'X' ELSE 'O' END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

ORA-00923: FROM keyword not found where expected 오류 난 문장
SELECT ANIMAL_ID, NAME, DECODE(SEX_UPON_INTAKE, 'Intact Male', 'X', 'Intact Female', 'X', 'O') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
*/

SELECT ANIMAL_ID, NAME, CASE WHEN REGEXP_LIKE(SEX_UPON_INTAKE, '^Neutered|^Spayed') THEN 'O' ELSE 'X' END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;