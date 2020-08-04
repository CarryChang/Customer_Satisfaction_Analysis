# -*- coding: utf-8 -*-
# @USER: CarryChang

# 设置词典大小为 n_features
n_features = 3000

# 存储断句的文件夹
sentence_cut_path = 'data/sentence_cut.txt'

# 主题句文件夹
topic_path = 'topic_text'

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

# 最大句子长度
maxlen = 100

# 最大的tokenizer字典长度
max_words = 1000

# 设置embedding大小
embedding_dim = 300

# train_method : 模型训练方式，默认 textcnn，可选：bilstm , gru
train_method = 'textcnn'

# 模型的保存位置，后续用于推理
sa_model_path_m = 'model_saved/model.h5'

# 离线保存tokenizer
tokenize_path = 'model_saved/tokenizer.pickle'