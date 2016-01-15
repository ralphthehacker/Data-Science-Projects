-- Does matrix multiplication on 2 matrices A and B
SELECT row_num,col_num, SUM(A.value*B.value)
FROM A,B
WHERE A.col_num = B.row_num
GROUP BY A.row_num,B.col_num