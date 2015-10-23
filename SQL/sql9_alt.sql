CREATE VIEW freq_ext AS
SELECT docid, term, count FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT MAX(val) FROM(
 SELECT y.docid, sum(c1 * c2) as val FROM
   (SELECT term, count c1
     FROM freq_ext
     WHERE docid = 'q') x, 
   (SELECT docid, term, count c2
     FROM freq_ext) y
    WHERE x.term = y.term
    GROUP BY y.docid
    ORDER BY val);





