f_train = open('train/train.tsv',newline='\n')
f_in = open('train/in.tsv','w',newline='\n')
f_ex = open('train/expected.tsv','w',newline='\n')

for line in f_train:
    a,b, _, _, text = line.split('\t')
    year = (float(a) + float(b)) / 2
    f_in.write(text)
    #f_in.write(text1 +" " + text2)
    f_ex.write(str(year) + '\n')

f_train.close()
f_in.close()
f_ex.close()


