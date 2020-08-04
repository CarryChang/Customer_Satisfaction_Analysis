# -*- coding: utf-8 -*-

from sa_analysis import topic_sa_analysis
import jieba.posseg as pseg
from sa_model_train import model_train
import multiprocessing
from setting import *
from tqdm import tqdm
import os

# 识别标点符号进行句子切分
def doc2sentence(resource_text):
    # jieba 预热
    print(pseg.cut('预热'))
    with open(sentence_cut_path, 'w', encoding='utf-8') as sentence_cut:
        for sentence in tqdm(resource_text):
            if len(sentence.strip()) > 1:
                for word, flag in pseg.cut(sentence):
                    if flag != 'x':
                        sentence_cut.write(word)
                    else:
                        sentence_cut.write('\n')

# 多线程主题句查询
def find_topic_sentence():
    if not os.path.exists(topic_path):
        os.mkdir(topic_path)
    task_split = []
    for topic_n, key_words_list in topic_words_list.items():
        task_split.append([topic_path, topic_n, key_words_list])
    # task multiprocessing
    thread_number = len(topic_words_list.keys())
    pool = multiprocessing.Pool(processes=thread_number)
    pool.map(find_key_txt, task_split)
def find_key_txt(data_list):
    sentence_cut = open(sentence_cut_path, 'r', encoding='utf-8')
    with open('{}/{}.txt'.format(data_list[0], data_list[1]), 'w', encoding='utf-8') as key_txt:
        for sentence in sentence_cut.readlines():
            for i in data_list[2]:
                if i in sentence:
                   key_txt.write(sentence)
    # 关闭文件
    sentence_cut.close()
    print('{} 已经查找完成'.format(data_list[1]))

if __name__ == '__main__':
    # 情感分析模型训练
    model_train()
    with open('data/text_resource.txt', 'r', encoding='utf-8') as resource_text:
        resource_text = resource_text.readlines()
        # 整句切分
        doc2sentence(resource_text)
        # 主题句查询
        find_topic_sentence()
        # 主题情感极性可视化
        topic_sa_analysis()
