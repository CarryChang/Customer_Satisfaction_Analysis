# -*- coding: utf-8 -*-
# @Time: 2020/6/20 0020 0:49
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 存储断句的文件夹
sentence_cut_path = 'data/sentence_cut.txt'
# 主题句
topic_path = 'topic_text'
# sentence length
maxlen = 100
# 使用字符级大大减少了字典的长度
max_words = 1000
embedding_dim = 300
# tokenize path
model_path = 'sa_model'
tokenize_path = 'sa_model/tokenizer.pickle'
# sa model path
sa_model_path = 'sa_model/c_cnn.h5'
# 基于字典的查找
topic_words_list = {
    '环境': {'环境', '周边', '风景', '空气', '江景', '小区', '景点', '夜景', '街', '周围', '景区', '声音', '景色'},
    '价格': {'价格', '房价', '性价比', '价位', '单价', '价钱'},
    '特色': {'特色', '装潢', '布置', '建筑', '结构', '格调', '装修', '设计', '风格', '隔音'},
    '设施': {'设施', '设备', '条件', '硬件', '房间', '热水', '马桶', '电梯', '阳台', '卫生间', '洗手间', '空调', '被子', '床', '大厅', '电话', '电', '摆设'},
    '餐饮': {'餐饮', '早餐', '咖啡', '味道', '饭', '菜', '水果', '特产', '餐', '美食', '烧烤', '宵夜', '食材', '饭馆', '小吃'},
    '交通': {'交通', '车程', '地段', '路程', '停车', '机场', '离', '车站', '地理', '位置', '地理', '中心', '海拔', '码头'},
    '服务': {'服务', '态度', '前台', '服务员', '老板', '掌柜', '店家', '工作人员'},
    '体验': {'体验', '整体', '感觉'},
}
# 存储情感极性的图
topic_emotion_pic = 'topic_emotion_pic'