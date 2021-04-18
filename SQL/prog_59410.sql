/*
https://programmers.co.kr/learn/courses/30/lessons/59410
*/

SELECT ANIMAL_TYPE, ifnull(NAME, 'No name') as NAME, SEX_UPON_INTAKE from ANIMAL_INS order by ANIMAL_ID;