import pandas as pd
import re
import json

df = pd.read_csv('dataset_text/train.csv', header=[0, 1])

test1 = "\"Hi\""
test2 = 'Hi, Hello'
test3 = u'Hi Hello AB A ZCGD АЛЁ'
test4 = 'Б.Ю. Александор А. Колмогоров'


re_quotes = r'\".*?\"'
re_uppercase = r'[A-ZА-Я]{1}\w+'
re_abbrev = r'[A-ZА-Я]{2,}'
re_name = r'[A-ZА-Я]\.'

#print(re.findall(re_quotes, test1))
#print(re.findall(re_uppercase, test2))
#print(re.findall(re_abbrev, test3))
#print(re.findall(re_name, test4))


dict_ = dict()

for i in range(df.shape[0]):
    string = df.iloc[i, 1]
    json_elem = {'sentence': string,
                 'quotes': re.findall(re_quotes, string)[::2],
                 'uppercase': re.findall(re_uppercase, string),
                 'abbrev': re.findall(re_abbrev, string),
                 'names': re.findall(re_name, string)}
    dict_[i] = json_elem

with open('dataset_text/dataset.json', 'w') as f:
    json.dump(dict_, f)


#with open('dataset_text/dataset.json', 'r') as f:
#    dataset = json.load(f)

#print(dataset)
