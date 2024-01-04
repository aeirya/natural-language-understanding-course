# MASSIVE data reader

import json
import random

def create_tokens_and_labels(id, sample):
    intent = sample['intent']
    utt = sample['utt']
    annot_utt = sample['annot_utt']
    tokens = utt.split()
    labels = []
    label = 'O'
    split_annot_utt = annot_utt.split()
    idx = 0
    BIO_SLOT = False
    while idx < len(split_annot_utt):
        if split_annot_utt[idx].startswith('['):
            label = split_annot_utt[idx].lstrip('[')
            idx += 2
            BIO_SLOT = True
        elif split_annot_utt[idx].endswith(']'):
            if split_annot_utt[idx-1] ==":":
                labels.append("B-"+label)
                label = 'O'
                idx += 1
            else:
                labels.append("I-"+label)
                label = 'O'
                idx += 1
            BIO_SLOT = False
        else:
            if split_annot_utt[idx-1] ==":":
                labels.append("B-"+label)
                idx += 1
            elif BIO_SLOT == True:
                labels.append("I-"+label)
                idx += 1
            else:
                labels.append("O")
                idx += 1

    if len(tokens) != len(labels):
        raise ValueError(f"Len of tokens, {tokens}, doesnt match len of labels, {labels}, "
                          f"for id {id} and annot utt: {annot_utt}")
    return tokens, labels, intent




sentences_tr, tags_tr, intent_tags_tr = [], [], []
sentences_val, tags_val, intent_tags_val = [], [], []
sentences_test, tags_test, intent_tags_test = [], [], []
all_tags, all_intents = [], []

for id, sample in enumerate(massive_raw):
    if sample['partition'] == 'train':
        tokens, labels, intent = create_tokens_and_labels(id, sample)
        sentences_tr.append(tokens)
         tags_tr.append(labels)
         intent_tags_tr.append(intent)




!gdown https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.0.tar.gz
!tar -xvf /content/amazon-massive-dataset-1.0.tar.gz

massive_raw_fa = []
with open('/content/1.0/data/fa-IR.jsonl', 'r') as f:
    for line in f:
        massive_raw_fa.append(json.loads(line))

    # Closing file
    f.close()

Read_Massive_dataset(massive_raw_fa)