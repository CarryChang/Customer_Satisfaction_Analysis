import os
def fina_analysis():
    file_path = 'score'
    try:
        os.mkdir(file_path)
        print(file_path+'文件夹已经建立，请查看当前文件路径')
    except Exception as e:
        print('文件夹已经存在，请查看当前程序路径')
    key_words = {'环境','娱乐','位置','价格','特色','设施','餐饮','交通','卫生','服务','体验'}
    for key_word in key_words:
        fina_analysis_1(key_word)
def fina_analysis_1(key_word):
    print(key_word)
    print('正在执行情感计算...')
    ##############看清楚对于‘r’的使用
    # key_txt_neg = open('key_emotion/%s_neg.txt'%key_word,'r',encoding='utf-8')
    # key_txt_pos = open('key_emotion/%s_pos.txt'%key_word,'r',encoding='utf-8')
    key_txt_neg_very = open('key_emotion/%s_neg_very.txt'%key_word,'r',encoding='utf-8')
    key_txt_pos_very = open('key_emotion/%s_pos_very.txt'%key_word,'r',encoding='utf-8')
    key_txt_neg_good = open('key_emotion/%s_neg_good.txt'%key_word,'r',encoding='utf-8')
    key_txt_pos_good = open('key_emotion/%s_pos_good.txt'%key_word,'r',encoding='utf-8')
    key_txt_common = open('key_emotion/%s_common.txt'%key_word,'r',encoding='utf-8')
    key_score = open('score/%s_total_score.txt'%key_word,'w',encoding='utf-8')
    score_pos_very = 0
    score_neg_very = 0
    score_pos_good = 0
    score_neg_good = 0
    common = 0
    for score in key_txt_pos_very:
        if score.startswith('0' or '1'):
            score_pos_very += float(score)
    key_score.write(key_word+'积极情绪总分')
    key_score.write(str(score_pos_very))
    key_score.write('\n')

    for score in key_txt_pos_good:
        if score.startswith('0' or '1'):
            score_pos_good += float(score)
    key_score.write(key_word+'积极情绪总分')
    key_score.write(str(score_pos_good))
    key_score.write('\n')

    for score in key_txt_neg_very:
        if score.startswith('0' or '1'):
            score_neg_very += float(score)
    key_score.write(key_word+'积极情绪总分')
    key_score.write(str(score_neg_very))
    key_score.write('\n')

    for score in key_txt_neg_good:
        if score.startswith('0' or '1'):
            score_neg_good += float(score)
    key_score.write(key_word+'积极情绪总分')
    key_score.write(str(score_neg_good))
    key_score.write('\n')

    for score in key_txt_common:
        if score.startswith('0' or '1'):
            ###########增加消极情绪极性
            common = 1 - float(score)
            score_neg_very += common
    key_score.write(key_word+'消极情绪总分')
    key_score.write(str(common))
    print(key_word+'评论打分分层统计完成')
    key_score.close()
if __name__ == '__main__':
    fina_analysis()
