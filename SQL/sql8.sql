SELECT val FROM(
   SELECT f1.docid d1, f2.docid d2, sum(f1.count * f2.count) val 
    FROM frequency f1, frequency f2 
     WHERE f1.term = f2.term
    AND f1.docid < f2.docid
     GROUP BY f1.docid, f2.docid)
   WHERE d1 = '10080_txt_crude' AND d2 = '17035_txt_earn';
