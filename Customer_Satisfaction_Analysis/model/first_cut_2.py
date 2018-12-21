from pyltp import Segmentor
from pyltp import Postagger
import os
def first_cut():
    ####在程序当前路径建立文件夹，文件名为train_txt
    file_path = 'key'
    try:
        os.mkdir(file_path)
        print(file_path+'文件夹已经建立，请查看当前文件路径')
    except Exception as e:
        print('文件夹已经存在，请查看当前程序路径')
    # #############初级分词，计算词频
    print('开始初级分词')
    #分词+选词
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    cont = open('resource_new.txt','r',encoding='utf-8')
    f1 = open('key/cut_all.txt','w',encoding='utf-8')
    f = open('key/only_n.txt','w',encoding='utf-8')
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('module/cws.model')  # 加载模型,不加载字典
    # segmentor.load_with_lexicon('cws.model', 'userdict.txt') # 加载模型,加载用户字典
    postagger = Postagger() # 初始化实例
    postagger.load('module/pos.model')  # 加载模型
    for sentence in cont:
        if sentence.strip() != '':
            words = segmentor.segment(sentence)  # 分词,不需要标注词性
            for word in words:
                f1.write(word+' ')
            f1.write('\n')
            word1 = segmentor.segment(sentence)  # 分词
            postags = postagger.postag(word1)  # 词性标注
            for word,tag in zip(word1,postags):
                if (tag == 'n' ):
                    f.write(word+' ')
            f.write('\n')
        else:continue
    f.close()
    segmentor.release()
    postagger.release()
if __name__ == '__main__':
    first_cut()
