from fairseq.models.roberta import  RobertaModel
from fairseq import hub_utils
from fairseq.models.roberta import RobertaModel, RobertaHubInterface

import os
from tqdm import tqdm


model_path = "model_finetuned"
loaded = hub_utils.from_pretrained(
    model_name_or_path=model_path,
    data_name_or_path=model_path,
    bpe="sentencepiece",
    sentencepiece_vocab=os.path.join(model_path, "sentencepiece.bpe.model"),
    load_checkpoint_heads=True,
    archive_map=RobertaModel.hub_models(),
    cpu=False
)
roberta = RobertaHubInterface(loaded['args'], loaded['task'], loaded['models'][0])

roberta.eval() 
roberta.cuda()
YEAR_MIN = 1814



preds = roberta.fill_mask('Ala <mask>, kota', topk=3)
#import pdb; pdb.set_trace()

def predict(f_in_path, f_out_path):
    dev_f_in = open(f_in_path,'r', newline='\n')
    dev_f_out = open(f_out_path,'w', newline='\n')

    for line in tqdm(dev_f_in,total = 19986):
        y_start,y_end, before, after = line.split('\t')
        before = ' '.join(before.split(' ')[-40:]) # tu można poprawić, żeby  śmigał na tokenal spm a nie zakładał że jest jak ze spacjami
        after = ' '.join(after.split(' ')[:40])
        input = before + ' <mask> ' + after
        year = (float(y_start) + float(y_end) ) / 2
        year = (year - YEAR_MIN) // 20
        year = str(int(year))
        input = str(year) + ' ' + input
        #import pdb; pdb.set_trace()
        preds = roberta.fill_mask(input, topk=10)
        hyps = []
        probs_sum = 0.0
        for pred in preds:
            if pred[2] == '<unk>':
                continue
            hyps.append(pred[2].rstrip().lstrip() + ':' + str(pred[1]))
            probs_sum += pred[1]
        hyps.append(':' + str(1 - probs_sum))
        preds_line = ' '.join(hyps)
        dev_f_out.write(preds_line + '\n')

    dev_f_out.close()
predict('../dev-0/in.tsv', '../dev-0/out.tsv')
predict('../dev-1/in.tsv', '../dev-1/out.tsv')
predict('../test-A/in.tsv', '../test-A/out.tsv')
