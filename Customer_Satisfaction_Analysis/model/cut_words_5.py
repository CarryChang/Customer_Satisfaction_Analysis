from pyltp import Segmentor
from pyltp import Postagger

def cut_words():
    #分词+去除空行
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    cont = open('resource_new.txt','r',encoding='utf-8')
    f = open('key/cut_resouce.txt','w',encoding='utf-8')
    segmentor = Segmentor()  # 初始化实例
    # segmentor.load('cws.model')  # 加载模型,不加载字典
    segmentor.load_with_lexicon('module/cws.model', 'userdict.txt') # 加载模型,加载用户字典
    postagger = Postagger() # 初始化实例
    postagger.load('module/pos.model')  # 加载模型
    for sentence in cont:
        if sentence.strip() != '':
            words = segmentor.segment(sentence)  # 分词
            pos_tags = postagger.postag(words)  # 词性标注
            for word,tag in zip(words,pos_tags):
                if tag != 'wp':
                    f.write(word)
                else:f.write('\n')
            f.write('\n')
        else:continue
    f.close()
    segmentor.release()
    postagger.release()
if __name__ == '__main__':
    cut_words()
    print('cut_words 完成')