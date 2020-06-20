import numpy as np
from sa_model_predict import SA
import matplotlib.pyplot as plt
from model_structure.conf import *
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def topic_sa_analysis():
    sa_model = SA()
    if not os.path.exists(topic_emotion_pic):
        os.mkdir(topic_emotion_pic)
        print(topic_emotion_pic+'文件夹已经建立，请查看当前文件路径')
    for key_word in topic_words_list.keys():
        sa_analysis_(key_word,sa_model)
def sa_analysis_(key_word,sa_model):
    print('{} 正在执行...'.format(key_word))
    key_txt = open('{}/{}.txt'.format(topic_path, key_word), 'r', encoding='utf-8').readlines()
    sentiments_score_predict = sa_model.predict(key_txt)
    sentiments_score_list = [i[0] for i in sentiments_score_predict]
    plt.hist(sentiments_score_list, bins=np.arange(0, 1, 0.01))
    plt.xlabel("情感值")
    plt.ylabel("评论数目")
    plt.title(key_word+'-情感极性分布图')
    plt.savefig('{}/{}.png'.format(topic_emotion_pic, key_word))
    plt.show()
    plt.close()
    print('{} 情感极性图完成'.format(key_word))
# if __name__ == '__main__':
#     # 增加批处理提升预测速度
#     topic_sa_analysis()
