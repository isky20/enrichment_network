for i in *b.csv;do python3 script_B.py $i 2;done 
python3 marge.py B.csv
rm *all.csv
for i in *b.csv;do python3 script_H.py $i 2;done 
python3 marge.py H.csv
rm *all.csv
for i in *b.csv;do python3 script_hb.py $i 2;done 
python3 marge.py HB.csv
rm *all.csv
Rscript com.r
