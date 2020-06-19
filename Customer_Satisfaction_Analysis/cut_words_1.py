import jieba
import jieba.posseg as pseg
from conf import *
def cut_sentence():
    resource = open('data/text_resource.txt', 'r', encoding='utf-8')
    repeat_filter = dict()

    with open(sentence_cut_path, 'w', encoding='utf-8') as sentence_cut:
        for sentence in resource.readlines():
            bos = ''
            for word, flag in pseg.cut(sentence):
                if flag != 'x':
                    bos += word
                else:
                    repeat_filter[bos] = ''
                    bos = ''
        # 去重清洗和分句
        for sentence_filter in repeat_filter.keys():
            sentence_cut.write(sentence_filter+'\n')
if __name__ == '__main__':
    # 解决标点符号分句的问题，jieba标点为x
    # words = pseg.cut("我爱北京天安门，南京。")  # jieba默认模式
    # for word, flag in words:
    #     print('%s %s' % (word, flag))
    print('开始断句')
    cut_sentence()
    print('断句完成')