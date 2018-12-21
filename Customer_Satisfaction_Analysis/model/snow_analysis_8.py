import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import os
def snow_analysis():
    file_path = 'emotion_pic'
    try:
        os.mkdir(file_path)
        print(file_path+'文件夹已经建立，请查看当前文件路径')
    except Exception as e:
        print('文件夹已经存在，请查看当前程序路径')
    key_words = {'环境','价格','特色','设施','餐饮','交通','服务','体验'}
    for key_word in key_words:
        snow_analysis_1(key_word)
def snow_analysis_1(key_word):
    print(key_word)
    sentiments_list = []
    print('正在执行...')
    key_txt = open('key_list/%s.txt'%key_word,'r',encoding='utf-8')
    key_txt_neg_very = open('key_emotion/%s_neg_very.txt'%key_word,'w',encoding='utf-8')
    key_txt_pos_very = open('key_emotion/%s_pos_very.txt'%key_word,'w',encoding='utf-8')
    key_txt_neg_good = open('key_emotion/%s_neg_good.txt'%key_word,'w',encoding='utf-8')
    key_txt_pos_good = open('key_emotion/%s_pos_good.txt'%key_word,'w',encoding='utf-8')
    key_txt_common = open('key_emotion/%s_common.txt'%key_word,'w',encoding='utf-8')
    for li in key_txt:
        s = SnowNLP(li)
        score = s.sentiments
        sentiments_list.append(score)
        if s.sentiments > 0.80000:
            key_txt_pos_very.write(li)
            key_txt_pos_very.write(str(score)+'\n')
        elif 0.6000 <= s.sentiments < 0.80000:
            key_txt_pos_good.write(li)
            key_txt_pos_good.write(str(score)+'\n')
        elif 0.4000 <= s.sentiments < 0.60000:
            key_txt_common.write(li)
            key_txt_common.write(str(score)+'\n')
        elif 0.2000 <= s.sentiments < 0.40000:
            key_txt_neg_good.write(li)
            key_txt_neg_good.write(str(score)+'\n')
        elif s.sentiments < 0.20000:
            key_txt_neg_very.write(li)
            key_txt_neg_very.write(str(score)+'\n')
    plt.hist(sentiments_list, bins=np.arange(0, 1, 0.01))
    plt.xlabel("情感值")
    plt.ylabel("评论数目")
    plt.title(key_word+'-情感极性分布图')
    plt.savefig('emotion_pic/%s.png'%key_word)
    ########不显示计算出的图
    # plt.show()
    #####记得使用完成后关闭
    plt.close()
    key_txt_pos_good.close()
    key_txt_pos_very.close()
    key_txt_neg_good.close()
    key_txt_neg_very.close()
    key_txt_common.close()
    print(key_word+'情感极性图完成')
if __name__ == '__main__':
    snow_analysis()
