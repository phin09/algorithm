/*
https://programmers.co.kr/learn/courses/30/lessons/62284
Oracle, MySQL 둘 다 가능
*/

SELECT a.CART_ID
FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') a, 
     (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') b
WHERE a.CART_ID= b.CART_ID
GROUP BY a.CART_ID
ORDER BY a.CART_ID;