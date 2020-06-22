MODEL=model_polish_roberta_base/sentencepiece.bpe.model
SPM=~/vcpkg/buildtrees/sentencepiece/x64-linux-dbg/src/spm_encode
${SPM} --model=${MODEL} <data/train.input0 >data/train.input0.spm.alllens
${SPM} --model=${MODEL} <data/dev.input0 >data/dev.input0.spm.alllens
