import pandas as pd
import re
import json
import logging

logging.basicConfig(filename='logger.log', level=logging.DEBUG, filemode='w')

test1 = "\"Hi\""
test2 = 'Hi, Hello'
test3 = u'Hi Hello AB A ZCGD АЛЁ'
test4 = 'Б.Ю. Александор А. Колмогоров'
test5 = '\n.'

re_quotes = r'\".*?\"'
re_uppercase = r'[A-ZА-Я]{1}\w+'
re_abbrev = r'[A-ZА-Я]{2,}'
re_name = r'[A-ZА-Я]\.'

delete = r"([MD]r?s?\.|\[.\]|'\'+|\.+)"


def make_dataset():
    json_dict = dict()
    count = 0
    for i in range(100, 150):
        string = re.sub(r'(\?+|\!+)', '.', df.iloc[i, 1])
        logging.warning(f'first step: {string}')
        string = re.sub(r'(\.{2,}|[-]+|[;:]+)', ' ', string)  # + ' '  delete ... ; - ;
        logging.warning(f'second step: {string}')
        string = re.sub(r'[^a-zA-Z0-9 \"\n\.]', '', string)  # delete excess symbols
        logging.warning(f'third step: {string}')
        sentences = re.split(r'\. ', string)

        for sentence in sentences:
            print('before: ', sentence, len(sentence))
            if '.' in sentence:
                sentence = re.sub(r'\.', '', sentence)
            print('after: ', sentence)
            if len(sentence) != 0:
                if len(sentence) < 4:
                    json_dict[count - 1]['name'].append(sentence + '.')
                else:
                    json_dict[count] = {'sentence': sentence,
                                        'quotes': re.findall(re_quotes, sentence),
                                        'uppercase': re.findall(re_uppercase, sentence),
                                        'abbrev': re.findall(re_abbrev, sentence),
                                        'name': re.findall(re_name, sentence)}
                    count += 1
            else:
                continue

    with open('dataset_text/dataset.json', 'w') as f:
        json.dump(json_dict, f)


"""
    Steps:
    1) ?,! -> .
    2) ..., -, $, ; -> ' '
    3) split example by . (but exclude cases Dr., Mr., etc)
    
    
"""

full_ = []
df = pd.read_csv('dataset_text/rt_reviews.csv', encoding='1251')
# print(df.head(10))

make_dataset()
