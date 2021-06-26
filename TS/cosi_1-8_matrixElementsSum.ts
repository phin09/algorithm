/*
https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
Arcade-Intro-8

column이 관건인 문제니 첫번째 for문을 column을 갖고 돌게 하는 게 나았음.
*/

function matrixElementsSum(matrix: number[][]): number {
    let total: number = 0;
    let badColumn: number[] = [];
    
    for (let i:number = 0; i < matrix.length; i++) {
        for (let j: number = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] === 0) badColumn.push(j)
            
            if (matrix[i][j] !== 0 && !badColumn.includes(j)) {
                total = total + matrix[i][j];                    
            }
        }
    }
    return total;
}
