CHUNK_SIZE = 500
def split_to_chunks(file_in_path, file_out_path):
    f_in = open(file_in_path)
    f_out = open(file_out_path,'w')

    for line in f_in:
        line = line.rstrip('\n')
        line_splitted = line.split(' ')
        for i in range(0,len(line_splitted), CHUNK_SIZE):
            to_write = ' '.join(line_splitted[i:i+CHUNK_SIZE])
            f_out.write(to_write + '\n')

    f_in.close()
    f_out.close()

split_to_chunks('data/dev.input0.spm','data/dev.input0.spmout')
