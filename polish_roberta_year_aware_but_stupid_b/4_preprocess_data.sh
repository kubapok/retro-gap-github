
fairseq-preprocess \
    --only-source \
    --trainpref "data/train.input0.spm" \
    --validpref "data/dev.input0.spm" \
    --destdir "data-bin/input0" \
    --workers 8 \
    --srcdict model_polish_roberta_base/dict.txt

#fairseq-preprocess \
#    --only-source \
#    --trainpref "data/train.label" \
#    --validpref "data/dev.label" \
#    --destdir "data-bin/label" \
#    --workers 8
