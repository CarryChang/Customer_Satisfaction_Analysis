import multiprocessing
from conf import *
import os
def find_topic_txts():
    if not os.path.exists(topic_path):
        os.mkdir(topic_path)
        print(topic_path+'文件夹已经建立，请查看当前文件路径')
    data_list_cube = []
    for topic_n, key_words_list in topic_words_list.items():
        data_list_cube.append([topic_path, topic_n, key_words_list])
    # 将数据进行分割和多线程计算并存储
    thread_number = len(topic_words_list.keys())
    pool = multiprocessing.Pool(processes=thread_number)
    # 每一个独立的thread独立负责一个支线
    pool.map(find_key_txt, data_list_cube)
def find_key_txt(data_list):
    sentence_cut = open(sentence_cut_path, 'r', encoding='utf-8')
    with open('{}/{}.txt'.format(data_list[0], data_list[1]),'w',encoding='utf-8') as key_txt:
        for sentence in sentence_cut.readlines():
            for i in data_list[2]:
                if i in sentence:
                   key_txt.write(sentence)
    sentence_cut.close()
    print('{} 已经查找完成'.format(data_list[1]))
# if __name__ == '__main__':
#     # 增加多进程
#     find_topic_txts()

