CREATE VIEW freq_ext1 AS
SELECT docid, term, count FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT MAX(val) FROM(
   SELECT f1.docid d1, f2.docid d2, sum(f1.count * f2.count) val 
    FROM freq_ext1 f1, freq_ext1 f2 
     WHERE f1.term = f2.term
    AND f1.docid < f2.docid
     GROUP BY f1.docid, f2.docid)
   WHERE d1 = 'q';






