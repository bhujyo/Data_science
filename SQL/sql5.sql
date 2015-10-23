SELECT count(*) FROM(
SELECT docid, count(term) as x 
   FROM frequency
   GROUP BY docid
     HAVING x > 300);
