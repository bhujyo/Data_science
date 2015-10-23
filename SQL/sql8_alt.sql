SELECT sum(c1 * c2) FROM
   (SELECT term, count c1
     FROM frequency
     WHERE docid = '10080_txt_crude') x, 
   (SELECT term, count c2
     FROM frequency
     WHERE docid = '17035_txt_earn') y
    WHERE x.term = y.term;
