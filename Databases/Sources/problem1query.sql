SELECT *
FROM Frequency
WHERE Frequency.docid = "10398_txt_earn"

-- PROBLEM 2

SELECT term
FROM Frequency
WHERE Frequency.docid = "10398_txt_earn" AND Frequency.count=1


-- Problem 3 Find the entries in both files that have a count of 1

SELECT term FROM Frequency WHERE Frequency.docid = "10398_txt_earn" AND Frequency.count = 1
UNION
SELECT term FROM Frequency WHERE Frequency.docid = "925_txt_earn" AND Frequency.count = 1

-- Problem 4: Find the documents that have any of the words Legal or Law

SELECT COUNT(*) FROM
    (
        SELECT UNIQUE * FROM Frequency
        WHERE Frequency.term = 'law' OR Frequency.term = 'legal'
    )

-- Problem 5: Count entries in the table that have more that 300 words on it

SELECT docid,COUNT(count) FROM Frequency
GROUP BY Frequency.docid
HAVING COUNT(count) > 300
