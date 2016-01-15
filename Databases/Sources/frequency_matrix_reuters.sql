SELECT A.docid,B.docid, SUM(A.count*B.count)
FROM Frequency as A, Frequency as B
WHERE A.term = B.term
GROUP BY A.docid,B.docid