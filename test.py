# coding:utf-8
from textda.data_expansion import data_expansion
import json

json_data = []
for line in open('./iflytek/train.json','r', encoding='utf-8'):
    json_data.append(json.loads(line))
dic = {}
f = open('./iflytek/train_new.json','w', encoding='utf-8')
for tmp in json_data:
    sen_list = data_expansion(tmp['sentence'], alpha_ri=0.1, alpha_rs=0)
    for sen in sen_list:
        dic = tmp
        dic['sentence'] = sen
        str_sen = json.dumps(dic, ensure_ascii=False)
        f.write(str_sen+'\n')







# from textda.youdao_translate import *
# dir = './data'
# translate_batch(os.path.join(dir, 'train'), batch_num=30)
