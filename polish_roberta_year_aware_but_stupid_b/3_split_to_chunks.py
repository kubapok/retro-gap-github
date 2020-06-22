CHUNK_SIZE = 500
YEAR_MIN = 1814
YEAR_MAX = 2013

def split_to_chunks(file_in_path, file_year_path, file_out_path, istrain):
    f_in = open(file_in_path)
    f_out = open(file_out_path,'w')
    f_year = open(file_year_path)
    
    for line in f_in:
        line_year = next(f_year)
        if istrain:
            a,b,_,_,_ = line_year.split('\t')
        else:
            a,b,_,_ = line_year.split('\t')

        year = int(( float(a) + float(b) ) / 2)
        year = (year - YEAR_MIN) // 20


        line = line.rstrip('\n')
        line_splitted = line.split(' ')
        for i in range(0,len(line_splitted), CHUNK_SIZE):
            to_write = '▁'  + str(year) + ' ' +  ' '.join(line_splitted[i:i+CHUNK_SIZE])
            f_out.write(to_write + '\n')

    f_in.close()
    f_out.close()

split_to_chunks('data/train.input0.spm.alllens', 'data/year_train.tsv', 'data/train.input0.spm',True)
split_to_chunks('data/dev.input0.spm.alllens', 'data/year_dev.tsv', 'data/dev.input0.spm', False)
